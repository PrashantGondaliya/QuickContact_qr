import base64
from io import BytesIO

import qrcode
from django.shortcuts import render

from .forms import ContactForm


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


def build_vcard(data):
    full_name = data.get("full_name", "")
    phone = data.get("phone", "")
    email = data.get("email", "")
    company = data.get("company", "")
    job_title = data.get("job_title", "")
    linkedin_url = data.get("linkedin_url", "")
    website = data.get("website", "")

    vcard_lines = [
        "BEGIN:VCARD",
        "VERSION:3.0",
        f"FN:{full_name}",
    ]

    if company:
        vcard_lines.append(f"ORG:{company}")

    if job_title:
        vcard_lines.append(f"TITLE:{job_title}")

    if phone:
        vcard_lines.append(f"TEL:{phone}")

    if email:
        vcard_lines.append(f"EMAIL:{email}")

    if linkedin_url:
        vcard_lines.append(f"URL:{linkedin_url}")

    if website:
        vcard_lines.append(f"URL:{website}")

    vcard_lines.append("END:VCARD")

    return "\n".join(vcard_lines)


def generate_qr_code_base64(data):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()
    image.save(buffer, format="PNG")

    image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return image_base64