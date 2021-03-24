import requests
import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_BKUSER')
EMAIL_PASSWORD = os.environ.get('EMAIL_BKPASS')

msg = EmailMessage()
msg['Subject'] = 'The email subject'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS

# request to docker compose repo for issues with beginner tag
docker_compose = requests.get(
    'https://github.com/docker/compose/issues?q=is%3Aopen+is%3Aissue+label%3Aexp%2Fbeginner')

if 'No results matched your search.' in docker_compose.text:
    msg.set_content('There is no issue for begginers on docker compose')
else:
    msg.set_content('Issue found on docker compose')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)

# with open('res.html', 'w', encoding="utf-8") as f:
#     f.write(r.text)
