from django.shortcuts import render

# Create your views here.
from django.core.mail import EmailMessage
from django.http import HttpResponse
import os

def send_assignment_email(request):
    # Email addresses
    to_email = 'tech@themedius.ai'
    cc_email = 'hr@themedius.ai'

    # Email content
    subject = 'Python (Selenium) Assignment - [Martin Simtaya]'
    body = """
    Dear Team,

    Please find attached the assignment submission, including the completed form screenshot, source code, resume, and other requested documents.

    Best regards,
    Martin Simtaya
    """

    # File attachments (ensure these files are in the specified directory)
    files_to_attach = [
        'files/screenshot.png',  # Form screenshot
        'files/source_code.zip',  # Source code
        'files/README.md',  # Documentation
        'files/resume.pdf',  # Resume
        'files/availability.txt',  # Availability confirmation
    ]

    # Create email
    email = EmailMessage(
        subject=subject,
        body=body,
        from_email='your-email@gmail.com',
        to=[to_email],
        cc=[cc_email],
    )

    # Attach files
    for file_path in files_to_attach:
        if os.path.exists(file_path):
            email.attach_file(file_path)
        else:
            return HttpResponse(f"File not found: {file_path}")

    # Send email
    try:
        email.send()
        return HttpResponse("Email sent successfully.")
    except Exception as e:
        return HttpResponse(f"Failed to send email: {e}")
