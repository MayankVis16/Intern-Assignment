import smtplib
import os
from email.message import EmailMessage
from mimetypes import guess_type

your_name = "Mayank Sharma"
semester = "Batch 2024"
branch = "Computer Science and Engineering"
roll_number = "2009091"


SENDER_EMAIL = "mayank.204216@gmail.com"  
SENDER_PASSWORD = "fpgc bjlw icca thmc"  
RECEIVER_EMAIL = "hr@ignitershub.com"

IMAGE_PATH = "C:\\Users\\Mayank Sharma\\Downloads\\WhatsApp Image 2025-02-27 at 18.14.39.jpg"

msg = EmailMessage()
msg["Subject"] = "Challenge 3 Completed"
msg["From"] = SENDER_EMAIL
msg["To"] = RECEIVER_EMAIL


msg.set_content(f"""
Hello HR Team,

I have completed Challenge 3. Here are my details:

Name: {your_name}
Semester: {semester}
Branch: {branch}
Roll Number: {roll_number}

Please find the attached image.

Best Regards,
{your_name}
""")


if os.path.exists(IMAGE_PATH):
    mime_type, _ = guess_type(IMAGE_PATH)
    if mime_type and mime_type.startswith("image/"): 
        with open(IMAGE_PATH, "rb") as img_file:
            msg.add_attachment(img_file.read(),
                               maintype="image",
                               subtype=mime_type.split("/")[-1],
                               filename=os.path.basename(IMAGE_PATH))
    else:
        print("Invalid file type! Only PNG, JPG, JPEG allowed.")
        exit(1)
else:
    print("Image file not found!")
    exit(1)


try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
