from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length, EqualTo


class SignupForm(FlaskForm):
    email = StringField(
            'Email',
            validators=[
                InputRequired(message='Email is required'),
                Email()
                ]
            )
    password = PasswordField(
            'Password',
            validators=[
                InputRequired('Password is required'),
                Length(min=8, max=30),
                EqualTo('confirm', message='Passwords must match')
                ]
            )
    confirm = PasswordField('Repeat Password')
    recaptcha = RecaptchaField()
