import os
import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from jinja2 import Environment, FileSystemLoader

SMTP_AUTH = os.environ['SMTP_AUTH']
SMTP_AUTH_SECRET = os.environ['SMTP_AUTH_SECRET']
SMTP_SERVER = os.environ['SMTP_SERVER'] or 'email-smtp.us-east-1.amazonaws.com'
SMTP_PORT = os.environ['SMTP_PORT'] or 587


def mail_sender(organization, username, user_email):
    fromaddr = 'IT Team <tech@mycompany.com>'
    toaddr = user_email
    filename = organization + '_' + username + '.zip'

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'VPN: User certificates'

    file_loader = FileSystemLoader('./')
    env = Environment(loader=file_loader)
    template = env.get_template('template/email.txt.j2')
    body = template.render(email=toaddr)
    msg.attach(MIMEText(body, 'plain'))

    attachment = open('/tmp/' + filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    filename = os.path.basename(filename)
    part.add_header('Content-Disposition', 'attachment; filename= %s' % filename)

    msg.attach(part)

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SMTP_AUTH, SMTP_AUTH_SECRET)
    text = msg.as_string()
    try:
        logging.debug('Sending email')
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        logging.info('Email successfully sent to %s', toaddr)
    except Exception as e:
        logging.warning(e)
