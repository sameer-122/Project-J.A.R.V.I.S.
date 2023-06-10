import smtplib
from email.message import EmailMessage
import ssl

def sendEmail(to, content):
    with open(r'D:\Jarvis\protocol.txt') as f:
        line = f.readlines()

    email_sender = 'bosssam29518@gmail.com'
    email_password =line[-1]    # os.environ.get("EMAIL_PASSWORD")

    email_receiver = to
    subject = content[:30]
    body = content

    em = EmailMessage()                     # Creating an object of EmailMessage class
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:       # 'smtp.gmail.com' is the email server
        smtp.login(email_sender,email_password)                                  # 465 is the port
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    print('Email sent')