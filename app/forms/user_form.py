from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, PasswordField
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


class FeeForm(FlaskForm):
    reg_no = StringField('Registration Number', validators=[DataRequired()], render_kw={"placeholder": "Enter Registration Number"})
    submit = SubmitField('Submit')


class FeeCollForm(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d', render_kw={"placeholder": "YYYY-MM-DD"})
    month = SelectField('Month', choices=[('jan', 'Jan'), ('feb', 'Feb'), ('mar', 'Mar'), ('apr', 'Apr'), ('may', 'May'), ('jun', 'Jun'), ('jul', 'Jul'), ('aug', 'Aug'), ('sep', 'Sep'), ('oct', 'Oct'), ('nov', 'Nov'), ('dec', 'Dec')], validators=[DataRequired()])
    type = SelectField('Type', choices=[('type_a', 'Type_A'), ('type_b', 'Type_B'), ('type_c', 'Type_C'), ('type_d', 'Type_D'), ('type_e', 'Type_E'), ('type_a1', 'Type_A1'), ('type_b1', 'Type_B1'), ('type_c1', 'Type_C1'), ('type_d1', 'Type_D1'), ('type_e1', 'Type_E1')], validators=[DataRequired()])
    mode = SelectField('Mode', choices=[('cash', 'Cash'), ('online', 'Online')], validators=[DataRequired()])
    slot = SelectField('Slot', choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening'), ('night', 'Night'), ('reserved', 'Reserved')], validators=[DataRequired()])
    submit = SubmitField('Submit')

