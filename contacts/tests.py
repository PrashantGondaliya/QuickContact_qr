from django.test import TestCase

from .forms import ContactForm
from .utils import build_vcard, escape_vcard_value


class ContactFormTests(TestCase):
    def test_valid_form_with_required_name_only(self):
        form = ContactForm(data={
            "full_name": "Prashant Gondaliya",
        })

        self.assertTrue(form.is_valid())

    def test_invalid_email_is_rejected(self):
        form = ContactForm(data={
            "full_name": "Prashant Gondaliya",
            "email": "not-an-email",
        })

        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)

    def test_invalid_phone_with_letters_is_rejected(self):
        form = ContactForm(data={
            "full_name": "Prashant Gondaliya",
            "phone": "hello123",
        })

        self.assertFalse(form.is_valid())
        self.assertIn("phone", form.errors)

    def test_non_linkedin_url_is_rejected_for_linkedin_field(self):
        form = ContactForm(data={
            "full_name": "Prashant Gondaliya",
            "linkedin_url": "https://example.com",
        })

        self.assertFalse(form.is_valid())
        self.assertIn("linkedin_url", form.errors)


class VcardUtilityTests(TestCase):
    def test_escape_vcard_value_escapes_special_characters(self):
        value = "ACME, Global; Tech"

        escaped_value = escape_vcard_value(value)

        self.assertEqual(escaped_value, "ACME\\, Global\\; Tech")

    def test_build_vcard_includes_basic_contact_details(self):
        data = {
            "full_name": "Prashant Gondaliya",
            "phone": "+44 7123 456789",
            "email": "prashant@example.com",
            "company": "QuickContact QR",
            "job_title": "Django Developer",
            "linkedin_url": "https://www.linkedin.com/in/prashant",
            "website": "https://example.com",
            "location": "London",
            "note": "Open to Django roles",
        }

        vcard = build_vcard(data)

        self.assertIn("BEGIN:VCARD", vcard)
        self.assertIn("VERSION:3.0", vcard)
        self.assertIn("FN:Prashant Gondaliya", vcard)
        self.assertIn("TEL;TYPE=CELL:+44 7123 456789", vcard)
        self.assertIn("EMAIL;TYPE=INTERNET:prashant@example.com", vcard)
        self.assertIn("END:VCARD", vcard)