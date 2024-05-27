from flask import render_template, Blueprint, request

mod = Blueprint('mod', __name__)

@mod.route('/')
def index():
    return render_template('index.html')


@mod.route('/auth', methods=['GET','POST'] )
def auth():
    if request.method =='POST':
        print(request.form.to_dict())   
    return render_template('auth.html')


@mod.route('/shop')
def shop():
    return render_template('shop.html')

@mod.route('/catalog')
def cat():
    return render_template('catalog.html')

@mod.route('/trash')
def trash():
    return render_template('trash.html')

@mod.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html')

@mod.route('/kitchen', methods=['GET', 'POST'])
def kitchen():
    return render_template('kitchen.html')

@mod.route('/product', methods=['GET', 'POST'])
def product():
    return render_template('product.html')
    

    
