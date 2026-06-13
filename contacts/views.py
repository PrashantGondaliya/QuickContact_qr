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

def escape_vcard_value(value):
    if not value:
        return ""

    return (
        str(value)
        .replace("\\", "\\\\")
        .replace(";", "\\;")
        .replace(",", "\\,")
        .replace("\n", "\\n")
    )

def build_vcard(data):
    full_name = escape_vcard_value(data.get("full_name", ""))
    phone = escape_vcard_value(data.get("phone", ""))
    email = escape_vcard_value(data.get("email", ""))
    company = escape_vcard_value(data.get("company", ""))
    job_title = escape_vcard_value(data.get("job_title", ""))
    linkedin_url = escape_vcard_value(data.get("linkedin_url", ""))
    website = escape_vcard_value(data.get("website", ""))
    location = escape_vcard_value(data.get("location", ""))
    note = escape_vcard_value(data.get("note", ""))

    vcard_lines = [
        "BEGIN:VCARD",
        "VERSION:3.0",
        f"FN:{full_name}",
        f"N:{full_name};;;;",
    ]

    if company:
        vcard_lines.append(f"ORG:{company}")

    if job_title:
        vcard_lines.append(f"TITLE:{job_title}")

    if phone:
        vcard_lines.append(f"TEL;TYPE=CELL:{phone}")

    if email:
        vcard_lines.append(f"EMAIL;TYPE=INTERNET:{email}")

    if linkedin_url:
        vcard_lines.append(f"URL;TYPE=LinkedIn:{linkedin_url}")

    if website:
        vcard_lines.append(f"URL;TYPE=Website:{website}")

    if location:
        vcard_lines.append(f"ADR;TYPE=WORK:;;{location};;;;")

    if note:
        vcard_lines.append(f"NOTE:{note}")

    vcard_lines.append("END:VCARD")

    return "\r\n".join(vcard_lines)


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