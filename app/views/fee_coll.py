# app/views/fee_coll.py
from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from wtforms import Form
from app.models.student import student
from app.models.fee import fee_coll
from app.forms.user_form import FeeForm, FeeCollForm

from app.utils.invoice_utils import generate_invoice_number
from datetime import datetime, date
from app import db
from app.utils.rate_utils import get_rate
from app.utils.telegram_utils import send_telegram_message
from app.utils.whatsapp_utils import send_whatsapp_message
from app.utils.email_utils import send_invoice_email

fee_coll_bp = Blueprint('fee_coll', __name__)

# Declare global variables
fee_coll_data = None
student_data = None


@fee_coll_bp.route('/search', methods=['GET', 'POST'])
def search():
    form = FeeForm()
    global student_data

    if request.method == 'POST' and form.validate_on_submit():
        reg_no = request.form.get('reg_no')
        student_data = student.query.filter_by(reg_no=reg_no).first()

        if student_data:
            return redirect(url_for('fee_coll.search_result', reg_no=reg_no))
        else:
            flash(f"No student found with registration number {reg_no}. Enter Registration number in Reg + 000 format. Eg. reg001", 'info')
    return render_template('fee_coll/search.html', form=form)

@fee_coll_bp.route('/search_result/<reg_no>', methods=['GET', 'POST'])
def search_result(reg_no):
    global fee_coll_data, student_data

    # Fetch data from both tables
    student_data = student.query.filter_by(reg_no=reg_no).first()
    fee_coll_data = fee_coll.query.filter_by(reg_no=reg_no).first()
    print(fee_coll_data)
    print(student_data)

    # Check if data exists for the given registration number
    if not student_data:
        flash('Student with registration number {} not found.'.format(reg_no), 'error')
        return redirect(url_for('fee_coll.search'))

    if not fee_coll_data:
        flash('Fee collection data for student with registration number {} not found.'.format(reg_no), 'error')
        return redirect(url_for('fee_coll.search'))
    
    # Render template with fetched data
    return render_template('fee_coll/search_result.html', student_data=student_data, fee_coll_data=fee_coll_data, form=FeeCollForm())

@fee_coll_bp.route('/collect_fee/<reg_no>', methods=['POST', 'GET'])
def collect_fee(reg_no):
    global fee_coll_data, student_data
    fee_coll_form = FeeCollForm()
    print('working till form declaration')
    student_data = student.query.filter_by(reg_no=reg_no).first()
    fee_coll_data = fee_coll.query.filter_by(reg_no=reg_no).first()

    if not student_data:
        flash(f'Student with registration number {reg_no} not found.', 'error')
        return render_template('errors/error.html')

    if not fee_coll_data:
        flash(f'Fee collection data for student with registration number {reg_no} not found.', 'error')
        return render_template('errors/error.html')

    if fee_coll_form.validate_on_submit():
        print('working till form validation')

        try:
            # Generate invoice number
            invoice_number = generate_invoice_number(fee_coll.query.order_by(fee_coll.id.desc()).first().invoice_number)  # type: ignore
            print('invoice_number', invoice_number)
            # Get rate based on form data
            type = fee_coll_form.type.data
            date_str = fee_coll_form.date.data
            print('date_str', date_str)
            print('type', type)
            cal_rate = get_rate(type, date_str)
            print('working till rate calculation')
            # Create a FeeColl instance
            fee_data = fee_coll(
                invoice_number=invoice_number,
                reg_no=reg_no,
                fee_time = date_str,
                payment_time=datetime.now(),
                username=session.get('username'),
                name=student.name,
                contact=student.contact,
                month=fee_coll_form.month.data,
                rate=cal_rate,
                type=type,
                slot=fee_coll_form.slot.data,
            ) # type: ignore
            # Add and commit to the database
            db.session.add(fee_data)
            db.session.commit()
            print('working till fee data')
            # Get chat ID and notice preferences from student
            chat_id = student.chat_id #type: ignore
            notice_preference = student.notice

            # Send notice based on preference
            if notice_preference == 'email':
                recipient_email = student.email
                success, error_message = send_invoice_email(recipient_email, student_data, fee_data) # type: ignore
                if success:
                    flash('Email sent successfully!', 'success')
                else:
                    flash(f"Error sending email: {error_message}", 'error')
            elif notice_preference == 'telegram':
                telegram_message = f"Thank You for your Interest in Vedaalay!\n" \
                                    f"-------\n" \
                                    f"Date: {fee_data.payment_time}\n \n" \
                                    f"Student's Name: {fee_data.name}\n" \
                                    f"Reg Number: {fee_data.reg_no}\n" \
                                    f"We will be sending all the other details shortly\n" \
                                    f"https://vedaalay.com/wp-content/uploads/2023/04/vedw.png/"
                success = send_telegram_message(chat_id, text=telegram_message)
                if success:
                    flash('Telegram message sent successfully!', 'success')
                else:
                    flash('Error sending Telegram message', 'error')
            elif notice_preference == 'whatsapp':
                whatsapp_message = f"Thank You for your Interest in Vedaalay!\n" \
                                    f"-------\n" \
                                    f"Date: {fee_data.payment_time}\n \n" \
                                    f"Student's Name: {fee_data.name}\n" \
                                    f"Reg Number: {fee_data.reg_no}\n" \
                                    f"We will be sending all the other details shortly\n" \
                                    f"https://vedaalay.com/wp-content/uploads/2023/04/vedw.png/"
                success = send_whatsapp_message(student.contact, whatsapp_message)
                if success:
                    flash('WhatsApp message sent successfully!', 'success')
                else:
                    flash('Error sending WhatsApp message', 'error')

            flash('Fee collected successfully!', 'success')
            return redirect(url_for('fee_coll.search'))

        except Exception as e:
            flash(f'Error processing fee collection: {str(e)}', 'error')

    return render_template('fee_coll/collect_fee.html', form=fee_coll_form, student_data=student_data)


@fee_coll_bp.route('/collect_fee/<reg_no>/success', methods=['POST', 'GET'])
def success():
    return render_template('fee_coll/success.html')