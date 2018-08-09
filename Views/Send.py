import os
import flask
import smtplib
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadTimeSignature

def send_email(email, msg):
	MY_ADDRESS = 'emailtestzione@gmail.com'
	PASSWORD = 'testing123!'

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(MY_ADDRESS, PASSWORD)
	server.sendmail(MY_ADDRESS, email, msg)
	server.quit()