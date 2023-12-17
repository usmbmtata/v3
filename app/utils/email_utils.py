from flask_mail import Message
from flask import current_app, render_template
from app import mail


def send_email(subject, recipients, template, **kwargs):
    sender = current_app.config['MAIL_DEFAULT_SENDER']
    message = Message(subject, sender=sender, recipients=recipients)
    email_body = render_template(template, **kwargs)
    message.html = email_body

    try:
        mail.send(message)
        return True, None
    except Exception as e:
        print(f"Error sending email: {e}")
        return False, str(e)


def send_otp_email(recipient_email, otp):
    try:
        subject = 'Verification Code For Registration'
        template = 'email/otp.html'  # You need to create this template
        return send_email(subject, [recipient_email], template, otp=otp)
    except Exception as e:
        print(f"Error sending email: {e}")
        return False, str(e)


def send_invoice_email(recipient_email, otp):
    try:
        subject = 'Verification Code For Registration'
        template = 'email/otp.html'  # You need to create this template
        return send_email(subject, [recipient_email], template, otp=otp)
    except Exception as e:
        print(f"Error sending email: {e}")
        return False, str(e)