from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
import datetime as dt
import os

app = Flask(__name__)
Bootstrap5(app)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


@app.route('/')
def home():
    return render_template('index.html', date=dt.date.today().year)

if __name__ == '__main__':
    app.run(debug=True)

