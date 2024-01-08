from calendar import month
from flask_mail import Message
from flask import current_app, render_template
from app import mail
from datetime import timedelta

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


def send_invoice_email(recipient_email, student_data, fee_data):
    try:
# Extracting data from student_data
        reg_no = student_data.reg_no
        reg_date = student_data.reg_date
        name = student_data.name
        course = student_data.course
        contact = student_data.contact
        address = student_data.address
        notice = student_data.notice

        # Extracting data from fee_data
        invoice_number = fee_data.invoice_number
        fee_time = fee_data.fee_time
        payment_time = fee_data.payment_time
        username = fee_data.username
        rate = fee_data.rate
        fee_type = fee_data.type
        slot = fee_data.slot
        mode = fee_data.mode

        #calculate end_date based on fee_time 
        end_date = fee_time + timedelta(days=30)
        subject = 'Invoice for the month of ' + str(fee_time.month)
        template = 'email/otp.html'  # You need to create this template
        return send_email(subject, [recipient_email], template, end_date=end_date, reg_no=reg_no, reg_date=reg_date, name=name, address=address, mode=mode, email=recipient_email)
    except Exception as e:
        print(f"Error sending email: {e}")
        return False, str(e)
    
