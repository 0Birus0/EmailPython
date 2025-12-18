import smtplib
from email.message import EmailMessage

def send_email():
    EMAIL_FROM = "boiggdoublecake@gmail.com"
    EMAIL_TO = "boiggdoublecake@gmail.com"
    EMAIL_PASSWORD = "orhwngejgkmkhhfw"


    msg = EmailMessage()
    msg.set_content("This is a test email from my Python app. 604PM anish test")
    msg["Subject"] = "Python Email Test"
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.send_message(msg)

    print("✅ Test email sent successfully!")


if __name__ == "__main__":
    send_email()
    print("success")