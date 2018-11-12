from flask import Flask, render_template, Markup, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

MyApp = Flask(__name__)
MyApp.config['SECRET_KEY'] = 'tistbas123'

class LoginForm(FlaskForm):
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
	remember = BooleanField('remember me')

@MyApp.route('/')
def index():
	return render_template('index.html')

@MyApp.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', form=form)


if __name__ == "__main__":
        MyApp.run()
