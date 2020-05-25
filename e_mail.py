from threading import Thread
from flask import Flask,render_template
from flask_mail import Mail, Message
from pub_api.instance.config import *


def send_email(to, subject, template, **kwargs):
    app = Flask(__name__)
    app.config.from_object('config')
    app.config.from_pyfile('instance/config.py')
    mail = Mail(app) 
    msg = Message(MAIL_SUBJECT_PREFIX + ' ' + subject,
                  sender=MAIL_SENDER, recipients=[to])
    with app.app_context():
        msg.body = render_template(template + '.txt', **kwargs)
        msg.html = render_template(template + '.html', **kwargs)
        mail.send(msg)
    print("Mail Sent")

