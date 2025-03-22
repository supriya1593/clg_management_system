import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

def send_otp2(data):
    
    otp2 = random.randint(1111,9999)

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    username = "supriyapuppy9@gmail.com"
    password = "zvfk pdyx royt uyfn"

    from_email = "supriyapuppy9@gmail.com"
    to_email = data
    subject = "OTP Validation"
    body = f"OTP for Validation is {otp2}. \nThank You."

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))

    server = smtplib.SMTP(smtp_server,smtp_port)
    server.starttls()
    server.login(username,password)
    server.send_message(msg)
    server.quit()

    return otp2
