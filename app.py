from flask import Flask, render_template, Markup, request, url_for

MyApp = Flask(__name__)

@MyApp.route('/')
def index():
	return render_template('index.html')


if __name__ == "__main__":
        MyApp.run()
