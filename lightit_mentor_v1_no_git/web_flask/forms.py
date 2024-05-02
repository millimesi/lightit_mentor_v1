from wtforms import Form, BooleanField, StringField, PasswordField, validators, SelectField
import pycountry


class RegistrationForm(Form):
    name = StringField('name', [validators.Length(min=4, max=25)])
    father_name = StringField('Father name', [validators.Length(min=4, max=25)])
    grand_father_name = StringField('Grand Father name', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    phone_number = StringField('phone number', [validators.Length(min=6, max=35)])
    user_type = SelectField('User Type', choices=[('parent', 'Parent'), ('student', 'Student')])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

class LoginForm(Form):
    email = StringField('Email', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [validators.DataRequired()])
    remember = BooleanField('Remember me')

# class RegistrationForm(FlaskForm):
#     name = StringField('Name', [validators.Length(min=2, max=25)])
    # father_name = StringField('Father Name')
    # grand_father_name = StringField('Grand Father Name')
    # email = StringField('Email')
    # country_code = SelectField('Country Code', 
    #                     choices=[(country.alpha_2, f"{country.name} (+{country.numeric})") for country in pycountry.countries])
    # phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=15)])
    # user_type = SelectField('User Type', 
    #                     choices=[('parent', 'Parent'), ('student', 'Student')], validators=[DataRequired()])
    # password = PasswordField('Password', validators=[DataRequired()])
    # confirm_password = PasswordField('Confirm Password')
    # submit = SubmitField('Sign up')

