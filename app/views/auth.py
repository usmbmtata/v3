import email
from email import message
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt
from app.models.admin import Admin
from app import db
import logging
from app.utils.email_utils import send_otp_email
from app.utils.otp_utils import generate_otp
import logging
from app.forms.user_form import LoginForm, admissionForm
from app.utils.telegram_utils import send_telegram_message
from app.utils.hash_utils import hash_aadhaar_number
from app.utils.registration_utils import generate_registration_number
from datetime import datetime, date
from app.models.student import student
from app.utils.whatsapp_utils import send_whatsapp_message
from app.models.fee_fare import Fee_Fare
from flask_wtf.csrf import CSRFProtect, generate_csrf

auth_bp = Blueprint('auth', __name__)
bcrypt = Bcrypt()

# Set the maximum login attempts
MAX_LOGIN_ATTEMPTS = 3


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    username = session.get('username')
    print(username)
    if session.get('username') is not None:
        return redirect('/dashboard/dashboard')

    if 'login_attempts' not in session:
        session['login_attempts'] = 0

    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if not username or not password:
            error_message = 'Username and password are required.'
            return render_template('auth/login.html', form=form, error=error_message)

        user = Admin.query.filter_by(username=username).first()  # Using SQLAlchemy to query the 'Admin' table

        if not user or not bcrypt.check_password_hash(user.password, password):
            session['login_attempts'] += 1
            attempts = session['login_attempts']
            print('Login attempts:Terminal', attempts)
            if session['login_attempts'] >= MAX_LOGIN_ATTEMPTS:
                print(f"Too many failed login attempts for user {username}")
                # Implement some temporary block mechanism, for example, lock the account/IP for a specific time
                return "Your account has been temporarily blocked due to multiple failed login attempts."

            error_message = 'Invalid username or password.'
            logging.warning(f'Failed login attempt for user {username}')
            return render_template('auth/login.html', form=form, error=error_message)

        session['username'] = username
        session.pop('login_attempts', None)  # Reset login attempts on successful login
        flash('Login successful ! Welcome to Vedaalay', 'success')
        logging.info(f'User {username} logged in')
        return redirect( url_for('dashboard.dashboard') )

    # If it's a GET request or the form did not validate on POST
    return render_template('auth/login.html', form=form)


@auth_bp.route('/logout')
def logout():
    # Remove the username from the session if it exists
    session.clear()

    return redirect(url_for('auth.login'))



@auth_bp.route('/admission', methods=['POST', 'GET'])
def admission():
    username = session.get('username')
    form = admissionForm()

    if request.method == 'POST' and form.validate_on_submit():
        print('form errors', form.errors)
        name = form.name.data
        course = form.course.data
        contact = form.contact.data
        email = form.email.data
        gender = form.gender.data
        registration_fee = 0 if form.registration_fee.data == 'yes' else 100
        address = form.address.data
        aadhar = hash_aadhaar_number(form.aadhar.data)
        mode = form.mode.data
        notice = form.notice.data
        code = form.code.data
        reg_date = form.date.data
        submission_time = datetime.now()
        pay_date = submission_time.date()

        # Generate registration number
        last_registration_number = student.query.order_by(student.reg_no.desc()).first()
        new_registration_number = generate_registration_number(last_registration_number)
        otp = generate_otp()
        # Send OTP via email
        send_otp_email(email, otp)

        new_student = student(
            name=name,
            course=course,
            contact=contact,
            email=email,
            gender=gender,
            registration_fee=registration_fee,
            address=address,
            aadhar_number=aadhar,
            mode=mode,
            notice=notice,
            code=code,
            reg_date=reg_date,
            pay_date=pay_date,
            reg_no=new_registration_number
        ) # type: ignore

        session['admission'] = {
            'name': name,
            'email': email,
            'otp': otp,
            'reg_no': new_registration_number
        }


        db.session.add(new_student)
        db.session.commit()
        username = session.get('username', None)
        chat_id = code

        if form.notice.data == 'email':
            recipient_email = form.email.data
            registration_fee = registration_fee
            name = form.name.data
            reg_no = new_registration_number
            success, error_message = send_otp_email(recipient_email, otp)
            if success:
                return render_template('auth/student_verify_otp.html', otp=otp)
            else:
                flash(f"Error sending email: {error_message}", 'error')

        elif form.notice.data == 'telegram':
            telegram_message = f"Thank You for your Interest in Vedaalay!\n" \
                            f"-------\n" \
                            f"Date: {reg_date}\n \n" \
                            f"Student's Name: {name}\n" \
                            f"Reg Number: {new_registration_number}\n" \
                            f"Registration Fee: {registration_fee}\n" \
                            f"we will be sending all the other details shortly\n" \
                            f"https://vedaalay.com/wp-content/uploads/2023/04/vedw.png/"
            success = send_telegram_message(chat_id, text=telegram_message)
            if not success:
                flash('Error sending Telegram message', 'error')
        elif form.notice.data == 'whatsapp':
            whatsapp_message = f"Thank You for your Interest in Vedaalay!\n" \
                            f"-------\n" \
                            f"Date: {reg_date}\n \n" \
                            f"Student's Name: {name}\n" \
                            f"Reg Number: {new_registration_number}\n" \
                            f"Registration Fee: {registration_fee}\n" \
                            f"Your OTP is {otp}\n" \
                            f"we will be sending all the other details shortly\n" \
                            f"https://vedaalay.com/wp-content/uploads/2023/04/vedw.png/"
            success = send_whatsapp_message(contact, whatsapp_message)
            if not success:
                flash("Error sending WhatsApp message", 'error')

    else:
        print('form errors', form.errors)
        flash('Admission form contains errors', 'error')
        return render_template('auth/admission.html', form=form)
    return render_template('auth/admission.html', form=form)


@auth_bp.route('/student_verify_otp', methods=['GET', 'POST'])
def student_verify_otp():
    admission = session.get('admission', {})
    name = admission.get('name')
    otp = admission.get('otp')
    reg_no = admission.get('reg_no')
    email = admission.get('email')

    if request.method == 'POST':
        entered_otp = request.form.get('otp')
        stored_otp = otp

        if entered_otp == stored_otp:
            session.clear()
            print('session cleared')

            success_message = 'Student added in the database successfully!'
            return redirect(url_for('auth.fee_coll'))

        else:
            flash('OTP you entered is incorrect, try again', 'error')
            return render_template('auth/student_verify_otp.html', otp=stored_otp, name=name, reg_no=reg_no, email=email)

    # Handle GET request when the page is initially loaded
    return render_template('auth/student_verify_otp.html')

@auth_bp.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    # Check if the message is a 'start' command
    if 'message' in data and 'text' in data['message'] and data['message']['text'] == '/start':
        # Get user ID
        chat_id = data['message']['chat']['id']

        # Send a welcome message
        send_telegram_message(chat_id, "Welcome to Vedaalay! Thank you for selecting Telegram. as a preffered method of communication. We will be sending all the other details shortly.")

    return '', 200