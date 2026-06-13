# QuickContact QR

QuickContact QR is a privacy-first Django web app that lets users generate QR codes containing their contact details.

The QR code stores the contact data directly as a vCard, so the generated QR code can work without relying on the website being online later.

## Features

- Contact form for name, phone, email, company, job title, LinkedIn, website, location, and note
- Email, URL, phone number, and LinkedIn URL validation
- vCard generation
- QR code generation from vCard data
- QR code size options
- QR reliability options for standard or high error correction
- Downloadable QR code image
- Downloadable `.vcf` contact card
- Privacy information page
- No database storage of submitted personal contact details
- Simple styling with Django static files
- Automated tests for forms, utilities, and views

## Privacy-first approach

QuickContact QR is designed to avoid storing submitted personal contact details in a database.

When a user submits the form, the app temporarily processes the details to generate a vCard and QR code, then returns the result to the browser.

The generated QR code itself contains the contact details. Anyone who scans the QR code may be able to read or save the information inside it, so users should only share QR codes with people they want to receive their contact information.

## How it works

```text
User fills in contact form
        ↓
Django validates the form
        ↓
App builds a vCard in memory
        ↓
App generates a QR code from the vCard
        ↓
User downloads or shares the QR code
```
No submitted contact details are intentionally saved to a database or file.

## Tech stack

- Python
- Django
- qrcode and Pillow libraries