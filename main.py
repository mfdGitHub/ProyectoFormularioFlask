from flask import Flask
from flask import render_template 
from flask import request
from flask import make_response
from flask import session

from flask import url_for 
from flask import redirect 

from flask_wtf import CSRFProtect
import forms

app = Flask(__name__)
app.secret_key = 'my_secret_key' #buena practica poner en variables de session os.get(variable_de_session)
csrf = CSRFProtect(app)


@app.route('/', methods = ['GET', 'POST'])
def index():
    comment_form = forms.ComentForm(request.form)
    if request.method == 'POST' and comment_form.validate():
        print (comment_form.username.data)
        print (comment_form.email.data)
        print (comment_form.comment.data)
    else:
        print ("Error en el formulario")

    #custome_cookie = request.cookies.get('custome_cookiess', 'Undefined')
    #print(custome_cookie)
    if 'username' in session:
        username = session['username']
        print(username)

    title = "Curso Flask"
    return render_template('index.html', title = title, form = comment_form)

@app.route('/logout')
def logout():
    if 'username'in session:
        session.pop('username')

    return redirect(url_for('login'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    login_form = forms.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        session['username'] = login_form.username.data

    return render_template('login.html', form = login_form)

@app.route('/cookie')
def cookie():
    response = make_response(render_template('cookie.html'))
    response.set_cookie('custome_cookie', 'Codigofacilito')
    return response

@app.route('/comment', methods = ['GET', 'POST'])
def comment():
    pass

if __name__=='__main__':
    app.run(debug=True, port=8000)

