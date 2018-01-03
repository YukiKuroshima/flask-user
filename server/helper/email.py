from flask_mail import Message
from server import mail


def send_email(to, title, body, sender='NO_REPLY_@jobhunting'):
    msg = Message(
            title,
            sender=sender,
            recipients=[to]
            )
    msg.body = body
    mail.send(msg)


def send_confirmation_email(to):
    title = 'Confirm email'
    body = 'Please confirm email'
    send_email(
            to=to,
            title=title,
            body=body
            )
