from flask import render_template, Blueprint, request

mod = Blueprint('mod', __name__)


@mod.route('/')
def index():
    return render_template('index.html')


@mod.route('/auth')
def auth():
    return render_template('auth.html')



@mod.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html')


    

    