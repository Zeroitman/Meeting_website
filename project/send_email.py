import smtplib
from trainees.settings import *


def send_notification(data):
    sender = EMAIL_HOST_USER
    sender_password = EMAIL_HOST_PASSWORD
    mail_lib = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT)
    mail_lib.login(sender, sender_password)
    emails = list(data.values())
    count = 1
    for name, email in data.items():
        txt = "Вы понравились пользователю: %s, его/её почта %s" % (name, email)
        msg = 'From: %s\r\nTo: %s\r\nContent-Type: text/plain; charset="utf-8"\r\nSubject: %s\r\n\r\n' % (
            sender, email, 'Тема сообщения')
        msg += txt
        mail_lib.sendmail(sender, emails[count], msg.encode('utf8'))
        count -= 1
    mail_lib.quit()
