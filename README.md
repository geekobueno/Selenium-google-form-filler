# Automated Form Filler and Email Sender

This repository contains two Python-based automation scripts:

1. **Google Form Automation**: A script using Selenium to fill out and submit a Google Form, complete with error handling and screenshot functionality.
2. **Automated Email Sender**: A Django-based solution to send emails with attachments, specifically designed for assignment submissions or similar use cases.

---

## **Google Form Automation**

### **Description**
This script automates the process of filling out a Google Form using Selenium. It verifies email inputs, captures screenshots at key steps, and handles errors gracefully.

### **Features**
- Automatically fills out form fields such as name, contact details, address, and more.
- Verifies the email address before form submission.
- Captures screenshots:
  - Before form submission (`form_filled_TIMESTAMP.png`)
  - After form submission (`form_submitted_TIMESTAMP.png`)
  - On encountering errors (`error_TIMESTAMP.png`)
- Graceful error handling and browser cleanup.

### **Setup Instructions**

#### **1. Install Dependencies**
```bash
pip install selenium
```

#### **2. Download ChromeDriver**
- Download the ChromeDriver version matching your installed Chrome browser from [here](https://chromedriver.chromium.org/downloads).
- Place it in the project directory or add its path to the `PATH` environment variable.

#### **3. Run the Script**
- Edit the `form_data` dictionary with your details:
  ```python
  form_data = {
      'full_name': 'Your Full Name',
      'contact': 'Your Contact Number',
      'email': 'Your Email Address',
      'address': 'Your Full Address',
      'pin_code': 'Your Pin Code',
      'dob': 'Your Date of Birth (MM/DD/YYYY)',
      'gender': 'Your Gender'
  }
  ```
- Execute the script:
  ```bash
  python form_automation.py
  ```
- The script will open the Google Form, fill in the details, and submit it. Screenshots will be saved in the same directory.

---

## **Automated Email Sender**

### **Description**
This Django application sends automated emails with file attachments, tailored for assignment submissions or similar tasks.

### **Features**
- Composes and sends an email with predefined recipients, subject, and body.
- Supports multiple file attachments from the `files` directory.
- Secure integration with an SMTP server.

### **Setup Instructions**

#### **1. Install Dependencies**
```bash
pip install django
```

#### **2. Configure SMTP**
- Open `settings.py` and add your SMTP credentials:
  ```python
  EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
  EMAIL_HOST = 'smtp.gmail.com'
  EMAIL_PORT = 587
  EMAIL_USE_TLS = True
  EMAIL_HOST_USER = 'your-email@gmail.com'
  EMAIL_HOST_PASSWORD = 'your-email-password'
  ```

#### **3. Add Attachments**
- Place required files (e.g., screenshots, source code, resume) in the `files` directory.

#### **4. Run the Application**
- Start the Django server:
  ```bash
  python manage.py runserver
  ```
- Access the `/send-email/` endpoint to send the email.

---

## **Combined Workflow**

1. **Step 1**: Run the Google Form automation script to fill and submit the form. Save the confirmation screenshot.
2. **Step 2**: Place the screenshots and other required files (e.g., resume, source code) in the `files` directory.
3. **Step 3**: Use the email sender script to send an email with all necessary attachments.

---

## **Requirements**
- Python 3.10 or higher
- Chrome browser and corresponding ChromeDriver
- Django for the email sender
- Selenium for the form automation

---

## **File Structure**
```
project/
├── form_automation.py        # Google Form automation script
├── mailer/                   # Django email sender app
│   ├── views.py              # Email logic
│   ├── urls.py               # Endpoint configuration
├── files/                    # Directory for attachments
│   ├── form_filled.png       # Form filled screenshot
│   ├── form_submitted.png    # Form submitted screenshot
│   ├── resume.pdf            # Resume file
│   ├── availability.txt      # Availability confirmation
├── settings.py               # Django settings
├── requirements.txt          # Dependencies
```
