from flask import Flask, render_template, Markup, request, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

MyApp = Flask(__name__)
MyApp.config['SECRET_KEY'] = 'tistbas123'
Bootstrap(MyApp)

class LoginForm(FlaskForm):
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
	remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
	email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
        password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

@MyApp.route('/')
def index():
	return render_template('index.html')

@MyApp.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', form=form)

@MyApp.route('/signup')
def signup():
	form = RegisterForm()
	return render_template('signup.html', form=form)


if __name__ == "__main__":
        MyApp.run()
