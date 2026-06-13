from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(
        max_length=100,
        label="Full name"
    )

    phone = forms.CharField(
        max_length=30,
        label="Phone number",
        required=False
    )

    email = forms.EmailField(
        label="Email address",
        required=False
    )

    company = forms.CharField(
        max_length=100,
        label="Company / workplace",
        required=False
    )

    job_title = forms.CharField(
        max_length=100,
        label="Job title",
        required=False
    )

    linkedin_url = forms.URLField(
        label="LinkedIn URL",
        required=False
    )

    website = forms.URLField(
        label="Website",
        required=False
    )