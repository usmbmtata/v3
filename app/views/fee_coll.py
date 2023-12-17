# app/views/fee_coll.py
from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from app.models.student import student
from app.models.fee import fee_coll
from app.utils.rate_utils import get_rate
from app.models.fee_fare import Fee_Fare
from app.forms.user_form import FeeForm, FeeCollForm
from app.forms.user_form import FeeForm  # Create this form in forms folder
from app.utils.invoice_utils import generate_invoice_number
from datetime import datetime
from app import db
from app.utils.telegram_utils import send_telegram_message
from app.utils.whatsapp_utils import send_whatsapp_message
from app.utils.email_utils import send_invoice_email

fee_coll_bp = Blueprint('fee_coll', __name__)


@fee_coll_bp.route('/search', methods=['GET', 'POST'])
def search():
    form = FeeForm()
    student_data = None
    fee_data = None

    if request.method == 'POST':
        if form.validate_on_submit():
            reg_no = request.form.get('reg_no')
            student_data = student.query.filter_by(reg_no=reg_no).first()

            if student_data:
                fee_data = fee_coll.query.filter_by(reg_no=reg_no).order_by(fee_coll.fee_time.desc()).first()

                if fee_data:
                    return render_template('fee_coll/search_result.html', student=student_data, fee=fee_data, form=form)
                else:
                    flash(f"No fee data found for registration number {reg_no}", 'error')
            else:
                flash(
                    f"No student found with registration number {reg_no} \n Enter Registration number in Reg + 000 format. Eg. reg001",
                    'error')
        else:
            flash("Form validation failed. Please check your inputs and try again.", 'error')

    return render_template('fee_coll/search.html', form=form)


@fee_coll_bp.route('/collect_fee/<reg_no>', methods=['GET', 'POST'])
def collect_fee(reg_no):
    student_data = student.query.filter_by(reg_no=reg_no).first_or_404()
    form = FeeForm()
    fee_coll_form = FeeCollForm()
    chat_id = student.chat_id
    if request.method == 'POST' and form.validate_on_submit() and fee_coll_form.validate_on_submit():
        invoice_number = generate_invoice_number(fee_coll.query.order_by(fee_coll.id.desc()).first().invoice_number)
        cal_rate = get_rate(fee_coll_form.type.data, fee_coll_form.date.data)
        print('here to check calculated rate',cal_rate)
        fee_data = fee_coll(
            invoice_number=invoice_number,
            reg_no=reg_no,
            fee_time=form.date.data,
            payment_time=datetime.now().date(),
            username=session.get('username'),
            name=student_data.name,
            contact=student_data.contact,
            month=fee_coll_form.month.data,
            rate = cal_rate,
            type=fee_coll_form.type.data,
            slot=fee_coll_form.slot.data,
        )

        db.session.add(fee_data)
        db.session.commit()

        if student.notice.data == 'email':
            recipient_email = student_data.email
            success, error_message = send_invoice_email(recipient_email, student_data, fee_data)
            if success:
                flash('Email sent successfully!', 'success')
            else:
                flash(f"Error sending email: {error_message}", 'error')

        elif fee_coll_form.notice.data == 'telegram':
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

        elif fee_coll_form.notice.data == 'whatsapp':
            whatsapp_message = f"Thank You for your Interest in Vedaalay!\n" \
                               f"-------\n" \
                               f"Date: {fee_data.payment_time}\n \n" \
                               f"Student's Name: {fee_data.name}\n" \
                               f"Reg Number: {fee_data.reg_no}\n" \
                               f"We will be sending all the other details shortly\n" \
                               f"https://vedaalay.com/wp-content/uploads/2023/04/vedw.png/"
            success = send_whatsapp_message(student_data.contact, whatsapp_message)
            if success:
                flash('WhatsApp message sent successfully!', 'success')
            else:
                flash('Error sending WhatsApp message', 'error')

        flash('Fee collected successfully!', 'success')
        return redirect(url_for('fee_coll.search'))

    return render_template('fee_coll/collect_fee.html', form=form, fee_coll_form=fee_coll_form, student=student_data)