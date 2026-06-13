from django.shortcuts import render

from .forms import ContactForm
from .utils import build_vcard, generate_qr_code_base64


def home(request):
    return render(request, "contacts/home.html")


def create_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            vcard_data = build_vcard(form.cleaned_data)
            qr_code_base64 = generate_qr_code_base64(vcard_data)

            return render(request, "contacts/qr_result.html", {
                "form_data": form.cleaned_data,
                "vcard_data": vcard_data,
                "qr_code_base64": qr_code_base64,
            })

    else:
        form = ContactForm()

    return render(request, "contacts/contact_form.html", {
        "form": form
    })