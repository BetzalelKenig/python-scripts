import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_BKUSER')
EMAIL_PASSWORD = os.environ.get('PYTHON_MAIL_PASS')
'''
server for tetsting
python -m smtpd -c DebuggingServer -n localhost:1025

'''
#conact to gmail at port 587
#with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
with smtplib.SMTP('localhost', 1025) as smtp:
	#idntafy arsalves wiht the mail server call auto in background
	# smtp.ehlo()
	# #enctipt the trafic
	# smtp.starttls()
	# smtp.ehlo()

	# smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

	subject = 'The email subject'
	body = 'The massage'

	msg = f'Subject: {subject}\n\n{body}'

	smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)
