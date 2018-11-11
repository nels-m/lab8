from flask import Flask, render_template, Markup, request, url_for

MyApp = Flask(__name__)

@MyApp.route('/')
def landing():
	return '<h1>This is a landing page for COSC419 Lab8. Here is more.</h1>'

if __name__ == "__main__":
        MyApp.run()
