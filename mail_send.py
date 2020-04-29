import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_BKUSER')
EMAIL_PASSWORD = os.environ.get('EMAIL_BKPASS')

msg = EmailMessage()
msg['Subject'] = 'The email subject'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS
msg.set_content('The massage')

with open('wolf.jpg', 'rb') as f:
	file_data = f.read()
	file_type = imghdr.what(f.name)
	file_name = f.name

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

	smtp.send_message(msg)
