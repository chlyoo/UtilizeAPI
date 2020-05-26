from pub_api.agent import *

@celery.task
def send_async_email(to, subject, template, **kwargs):
    msg = Message(MAIL_SUBJECT_PREFIX + ' ' + subject,
                  sender=MAIL_SENDER, recipients=[to])
    with app.app_context():
        msg.body = render_template(template + '.txt', **kwargs)
        msg.html = render_template(template + '.html', **kwargs)
        mail.send(msg)
    print("Mail Sent")
