import os
import flask
from flask import Flask, session, request, redirect, url_for, render_template
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadTimeSignature
from EncryptedMessages.views.Send import send_email
import smtplib


s = URLSafeTimedSerializer('EncryptDisBoi')

@EncryptedMessages.app.route('/confirmemail/<email>', methods=['GET','POST'])
def confirmemail(email):
	if request.method == 'GET':
		token = s.dumps(email, salt='email-confirm')
		link = url_for('confirm_email', token= token, _external= True)
		msg = '\nYour account has been activated click the link to confirm your account and login! Your link is {}'.format(link)
		send_email(email, msg)
	return flask.render_template("confirmemail.html", email = email)

@ticketing.app.route('/confirm_email/<token>')



def confirm_email(token):
	try:
		#have two hours to confirm
		email = s.loads(token, salt= 'email-confirm', max_age= 7200)
	except SignatureExpired:
		return flask.render_template('Phrases.html', TimeOut = True)
	except BadTimeSignature:
		return flask.render_template('Phrases.html', WrongLink = True)
	list_col = ['IsValid']
	list_val = ['True']
	update_user_data_email(list_col, list_val, email)
	return redirect(url_for("login"))
