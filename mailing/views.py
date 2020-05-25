from datetime import datetime
from flask import render_template, session, redirect, url_for, flash
from . import mailing
from .forms import registerform
from ..e_mail import *


@mailing.route('/register', methods=['GET', 'POST'])
def register():
	form=registerform
	if form.validate_on_submit():
		"""
		collection = db.get_collection('emails')
		collection.insert_one(form.email.data)
		send_email(form.email.data, 'Successfully added to our mailing list.', 'email/registered')
		flash('Welcome Email has been sent.')
		"""
	return render_template('register.html')
