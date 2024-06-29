import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import dotenv

def send_email(receiver_email, sender_email, email_subject, email_message):
    # smpt settings
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = os.getenv('SMTP_USERNAME')
    smtp_password = os.getenv('SMTP_PASSWORD')
    
    # create the email
    email_msg = MIMEMultipart()
    email_msg['From'] = send_email
    email_msg['To'] = receiver_email
    email_msg['Subject'] = email_subject
    
    email_msg.attach(MIMEText(email_message, 'plain'))
    
    with smtplib.SMTP(smtp_server, smtp_port) as eserver:
        eserver.starttls()
        eserver.login(smtp_username, smtp_password)
        eserver.sendmail(sender_email, receiver_email, email_message)

    print(f"Email sent successfully to {receiver_email}")

if __name__ == '__main__':
    receiver_email = input("Enter receiver's email address: ")
    sender_email = input("Enter your email address: ")
    subject = input("Enter the subject: ")
    message = input("Enter the message: ")

    send_email(receiver_email, sender_email, subject, message)
