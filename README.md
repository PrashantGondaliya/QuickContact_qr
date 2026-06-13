# QuickContact QR

QuickContact QR is a privacy-first Django web app that lets users generate a QR code containing their contact details.

The QR code stores the contact data directly as a vCard, so the app does not need to save personal information in a database.

## Features

- Contact form for name, phone, email, company, job title, LinkedIn, website, location, and note
- Form validation for email, URLs, phone number, and LinkedIn URL
- vCard generation
- QR code generation
- Downloadable QR code image
- No database storage of submitted personal contact details
- Simple responsive styling with Django static files

## Privacy-first approach

This app does not intentionally store submitted contact details.

The submitted information is used temporarily to generate a vCard QR code and is returned to the user in the browser.

Anyone who scans the QR code can read the contact details inside it, so users should only share QR codes with people they want to share their contact information with.

## Tech stack

- Python
- Django
- HTML
- CSS
- qrcode
- Pillow

