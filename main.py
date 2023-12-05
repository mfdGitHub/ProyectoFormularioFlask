from flask import Flask
from flask import render_template 
from flask import request
from flask import make_response
from flask import session
from flask import flash 
from flask import g 
from flask import url_for 
from flask import redirect 

from config import DevelopmentConfig
from models import db 
from models import User

from flask_wtf import CSRFProtect
import forms
import json 

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.errorhandler(401)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.before_request 
def before_request():
    g.test = 'test1'

@app.route('/', methods = ['GET', 'POST'])
def index():
    print(g.test)
    contact_form = forms.ComentForm(request.form)
    if 'username' in session:
        username = session['username']
        print(username)
        
    title = "Index"
    return render_template('index.html', title = title, form = contact_form)

@app.after_request
def after_request(response):
    print(g.test)
    return response 

@app.route('/logout')
def logout():
    if 'username'in session:
        session.pop('username')

    return redirect(url_for('login'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    login_form = forms.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        username = login_form.username.data
        success_message = 'Bienvenido {}'.format(username)
        flash(success_message)
        session['username'] = login_form.username.data

    return render_template('login.html', form = login_form)

@app.route('/create', methods = ['GET','POST'])
def create():
    create_form = forms.CreateForm(request.form)
    if request.method == 'POST' and create_form.validate():
        
        user = User(create_form.username.data,
                    create_form.password.data,
                    create_form.email.data)
        
        db.session.add(user)
        db.session.commit()

        username = create_form.username.data 
        success_message = 'Usuario registrado en la base de datos'
        flash(success_message)

    return render_template('create.html', form = create_form)

@app.route('/cookie')
def cookie():
    response = make_response(render_template('cookie.html'))
    response.set_cookie('custome_cookie', 'Codigofacilito')
    return response

@app.route('/comment', methods = ['GET', 'POST'])
def comment():
    pass
@app.route('/ajax-login', methods = ['POST'])
def ajax_login():
    print(request.form)
    username = request.form['username']
    response = {'status': 200, 'username': username, 'id': 1 }
    return json.dumps(response)

if __name__=='__main__':
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.run(port=8000)

