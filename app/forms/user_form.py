from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, RadioField, SelectField, PasswordField
from wtforms.validators import DataRequired, Email, Length
class admissionForm(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d', render_kw={"placeholder": "YYYY-MM-DD"})
    name = StringField('Name', render_kw={"placeholder": "First Name  Last Name"})
    course = StringField('Course', render_kw={"placeholder": "Course Name"})
    contact = StringField('Contact Number', validators=[Length(min=10, max=10)], render_kw={"type": "tel", "pattern": "[0-9]*", "placeholder": "Enter Phone Number"})
    email = StringField('Email', validators=[Email()], render_kw={"placeholder": "Enter Email Address"})
    gender = SelectField('Gender', choices=[('Select', 'Select'), ('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    registration_fee = SelectField('Reg Discount', choices=[('Select', 'Select'), ('yes', 'Yes'), ('no', 'No')])
    address = StringField('Address', render_kw={"placeholder": "Locality"})
    aadhar = StringField('Aadhaar Number', validators=[Length(min=12, max=12)], render_kw={"type": "tel", "pattern": "[0-9]*", "placeholder": "Enter Aadhaar Number"})
    mode = SelectField('Payment Mode', choices=[('Select', 'Select'), ('online', 'Online'), ('cash', 'Cash')])
    notice = SelectField('Notification Mode', choices=[('Select', 'Select'), ('whatsapp', 'WhatsApp'), ('telegram', 'Telegram'), ('email', 'Email')])
    code = StringField('Code', validators=[Length(min=10, max=10)], render_kw={"type": "tel", "pattern": "[0-9]*", "placeholder": "Enter Code"})
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "Enter Username"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Write your password"})
    submit = SubmitField('Login')


