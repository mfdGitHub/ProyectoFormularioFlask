#from wtforms import Form 
from wtforms import Form 
from wtforms import StringField
from wtforms import PasswordField
from wtforms.fields import EmailField
from wtforms import HiddenField
from wtforms import validators
from models import User

def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio.')


class CommentForm(Form):    
    comment = StringField('Comentario',
                [
                    validators.DataRequired(message = 'El username es requerido!!!')
                ])


class LoginForm(Form):
    username = StringField('Username',
                [
                    validators.DataRequired(message = 'El username es requerido!!!'),
                    validators.length(min=4, max=25, message='Ingrese un username valido!!!')
                ])
    password = PasswordField('Password', 
                [
                    validators.DataRequired(message='El password es requerido!!')
                ])

class CreateForm(Form):
    username = StringField('Username',
                [
                    validators.DataRequired(message = 'El username es requerido!!!'),
                    validators.length(min=4, max=25, message='Ingrese un username valido!!!')
                ])
    email = EmailField('Correo electronico',
            [
                validators.DataRequired(message = 'El email es requerido'),
                validators.Email(message='Ingresa un email valido!!'),
                validators.length(min=4, max=50, message='Ingrese un email valido!!!')
            ])
    password = PasswordField('Password',
                [
                    validators.DataRequired(message='El passowrd es requerido!!!')
                ])

    def validate_username(form, field):
        username = field.data 
        user = User.query.filter_by(username = username).first()
        if user is not None:
            raise validators.ValidationError('El username ya se encuentra registrado!!!')