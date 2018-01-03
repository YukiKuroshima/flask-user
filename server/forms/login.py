from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length


class LoginForm(FlaskForm):
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
                InputRequired(),
                Length(min=8, max=30)
                ]
            )
    remember = BooleanField('remember me')
    recaptcha = RecaptchaField()
