from flask_mail import Mail, Message
from flask import render_template
from config import Config

mail = Mail()

class Sendmail():
    def __init__(self, subject, recipients):
        self.subject = subject
        self.sender = Config.MAIL_USERNAME
        self.recipients = recipients
        self.html = None
        
    def send_email(self, template, **kwargs):
        msg = Message(self.subject, sender=self.sender, recipients=self.recipients)
        msg.html = render_template(template, **kwargs)
        mail.send(msg)