from smtplib import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime


# --------------------------- SNMP CONNECTION SETUP -----------------------------------

def send_gmail(from_email: str, to_email: str, password: str,
               subject: str, message: str, port: int = 587, gmail_server: str = 'smtp.gmail.com'):
    """
    Simple Function to Send GMAIL Email.

    :param password: Gmail APP Password
    :param gmail_server: Gmail server
    :param from_email: Senders Email
    :param to_email: Receivers Email
    :param subject: Title of Email
    :param message: Email Message
    :param port: Default Port 587
    :return: None
    """
    with SMTP(gmail_server, port=port) as connection:
        connection.starttls()
        connection.login(from_email, password)

        msg = MIMEMultipart()

        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # add in the message body
        msg.attach(MIMEText(message, 'html'))
        connection.send_message(msg)

        # print(msg)
        print("Email Sent!")
        connection.quit()

    return msg


def main():
    from creds import GMAIL_SERVER, FROM_ADDRESS, TO_ADDRESS, PASSWORD, SUBJECT
    send_gmail(gmail_server=GMAIL_SERVER, from_email=FROM_ADDRESS, to_email=TO_ADDRESS, subject=SUBJECT,
               password=PASSWORD, message=MESSAGE)


if __name__ == '__main__':
    # --------------------------- SNMP VARIABLES -----------------------------------
    SUBJECT = 'Testing Email Functionality'
    MESSAGE = f'Testing Email Functionality on {datetime.utcnow()}'
    # --------------------------- TEST FUNCTION -----------------------------------
    main()
