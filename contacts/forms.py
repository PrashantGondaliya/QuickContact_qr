import re

from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(
        max_length=100,
        label="Full name",
        widget=forms.TextInput(attrs={
            "placeholder": "e.g. Prashant Gondaliya"
        })
    )

    phone = forms.CharField(
        max_length=30,
        label="Phone number",
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "e.g. +44 7123 456789"
        })
    )

    email = forms.EmailField(
        label="Email address",
        required=False,
        widget=forms.EmailInput(attrs={
            "placeholder": "e.g. prashant@example.com"
        })
    )

    company = forms.CharField(
        max_length=100,
        label="Company / workplace",
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "e.g. QuickContact QR"
        })
    )

    job_title = forms.CharField(
        max_length=100,
        label="Job title",
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "e.g. Django Developer"
        })
    )

    linkedin_url = forms.URLField(
        label="LinkedIn URL",
        required=False,
        widget=forms.URLInput(attrs={
            "placeholder": "e.g. https://www.linkedin.com/in/your-name"
        })
    )

    website = forms.URLField(
        label="Website",
        required=False,
        widget=forms.URLInput(attrs={
            "placeholder": "e.g. https://yourwebsite.com"
        })
    )

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")

        if not phone:
            return phone

        allowed_pattern = r"^[0-9+\-\s()]+$"

        if not re.match(allowed_pattern, phone):
            raise forms.ValidationError(
                "Phone number can only contain numbers, spaces, +, -, and brackets."
            )

        digits_only = re.sub(r"\D", "", phone)

        if len(digits_only) < 7:
            raise forms.ValidationError(
                "Phone number seems too short."
            )

        if len(digits_only) > 15:
            raise forms.ValidationError(
                "Phone number seems too long."
            )

        return phone

    def clean_linkedin_url(self):
        linkedin_url = self.cleaned_data.get("linkedin_url")

        if not linkedin_url:
            return linkedin_url

        if "linkedin.com" not in linkedin_url.lower():
            raise forms.ValidationError(
                "Please enter a valid LinkedIn URL."
            )

        return linkedin_url

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name", "").strip()

        if len(full_name.split()) < 2:
            raise forms.ValidationError(
                "Please enter your full name, including first and last name."
            )

        return full_name