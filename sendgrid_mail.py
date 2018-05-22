# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *

def send_notification(mail_from, mail_to, subject, msg):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email(mail_from)
    to_email = Email(mail_to)
    content = Content("text/plain", msg)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    if response.status_code != 202:
        print('Sending failed')
    else:
        print('Notification mail sent')
