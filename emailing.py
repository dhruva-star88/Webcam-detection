import smtplib
import imghdr
from email.message import EmailMessage
import os

PASSWORD = os.getenv("WEBCAM_DETECTION")
SENDER = "workdhruvateja@gmail.com"
RECEIVER = "dhruvatej6565@gmail.com"


def send_email(image_path):
    print("send_email function has started")
    email_message = EmailMessage()
    email_message["Subject"] = "New Object has detected"
    email_message.set_content("Hey, we just detected something")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))
    # Create host to send gmail
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

    print("Email Sent")


if __name__ == "__main__":
    send_email("images/91.png")
