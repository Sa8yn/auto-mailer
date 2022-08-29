from email.message import EmailMessage
from lepass import password
import ssl
import smtplib

email_sender = 'vaibhavsatish9@gmail.com'
email_password = password

email_reciever = 'canigo4803@rxcay.com'

subject = "test subject for email sender python project"

body = """ The test body for auto email sender python project.
this is the body this is the body
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())
