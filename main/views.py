from datetime import datetime
from flask import render_template, session, redirect, url_for, flash
from flask_login import current_user, login_user, login_required, logout_user
from . import main
from .forms import NameForm
import pygsheets
from ..e_mail import *
GOOGLE_SERVICE_KEY='/data/myapp/pub_api/instance/pubapi.json'
GOOGLE_SPREADSHEET_NAME='publicdata'
GOOGLE_WORKSHEET='Sheet'
#authorization
gc = pygsheets.authorize(service_file=GOOGLE_SERVICE_KEY)
sh = gc.open(GOOGLE_SPREADSHEET_NAME)
wks = sh.worksheet('title', GOOGLE_WORKSHEET)

@main.route('/', methods=['GET', 'POST'])
def index():
	list=wks.get_row(row=2)[1:21]
	if int(list[5])>50:
		flash("Air is not so good")
		

	return render_template('index.html', list=list,url_for=url_for,
							current_time=datetime.utcnow())
