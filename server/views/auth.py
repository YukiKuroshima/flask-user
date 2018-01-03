from flask import Blueprint, request, render_template, redirect, \
        url_for, session
from server.forms.signup import SignupForm
from server.models.user import User
from sqlalchemy.exc import IntegrityError
from server.helper.email import send_confirmation_email
import smtplib


auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    """ Sign up user """
    form = SignupForm()
    if form.validate_on_submit():
        new_user = User(email=form.email, password=form.password)
        try:
            new_user.save()
            session['unconfirmed_email'] = form.email.data
            return redirect(url_for('auth.confirm'))
        except IntegrityError as e:
            form.email.errors.append('This email is taken')

    # Render template iff `GET` or validation did not pass
    return render_template('signup.html', form=form)


@auth_blueprint.route('/confirm')
def confirm():
    """ Confirm user's email """
    try:
        send_confirmation_email(session['unconfirmed_email'])
    except smtplib.SMTPRecipientsRefused:
        msg = """
            We tried to send you a confirmatoin email but it seems that your email does not exist.
            Are you sure "{0}" is correct?
            Please go back to sign up page and re-enter your information
            """

        return render_template('confirm.html',
                email=session['unconfirmed_email'],
                msg=msg.format(session['unconfirmed_email']))

    return render_template('confirm.html', email=session['unconfirmed_email'])
