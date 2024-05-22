from flask import Flask, request, render_template
from peewee
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/auth')
def auth():
    return render_template('auth.html')

@app.route('/profie/<id>')
def profile():
    return render_template('')


if __name__=='__main__':
    app.run()