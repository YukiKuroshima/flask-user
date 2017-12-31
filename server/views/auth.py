from flask import Blueprint, request, render_template, redirect, url_for


auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/signup')
def signup():
    """ Sign up user """
    # Create user
    # Render template
    return render_template('signup.html')
