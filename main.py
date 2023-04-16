import smtplib
from functions import get_data
from init import sender_email, sender_password, smtp_server, smtp_port
from email.mime.multipart import MIMEMultipart
from jinja2 import Template


def send_emails():
    try:
        smtp = smtplib.SMTP(smtp_server, smtp_port)
        smtp.starttls()
        smtp.login(sender_email, sender_password)
    except Exception:
        print('Неправильно заданная почта отправителя или пароль')
    else:
        attributes = get_data()
        html = open(attributes[1]).read()
        temp = Template(html)
        for user in attributes[0]:
            if user:
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = user[2]
                msg['Subject'] = attributes[2]
                msg.add_header('Content-Type', 'text/html')
                gen_html = temp.render(name=user[0], surname=user[1], mail=user[2])
                msg.set_payload(gen_html)
                try:
                    smtp.sendmail(msg['From'], msg['To'], msg.as_string())
                except smtplib.SMTPRecipientsRefused:
                    print(f'Пользователя {msg["To"]} не существует, сообщение ему не отправлено')
                    continue
        smtp.quit()


if __name__ == '__main__':
    send_emails()
