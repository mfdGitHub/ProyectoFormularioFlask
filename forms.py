#from wtforms import Form 
from wtforms import Form 
from wtforms import StringField
from wtforms.fields import EmailField

from wtforms import validators


def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio.')

class ComentForm(Form):
    username = StringField('username', 
            [
                validators.DataRequired(message = 'El username es requerido'),
                validators.length(min=4, max=25, message="Ingrese un username valido!!!")
                
            ] 
            )
    email = EmailField('Correo electronico',
            [
                validators.DataRequired(message = 'El email es requerido'),
                validators.Email(message='Ingresa un email valido!!')
            ])
    comment = StringField('Comentario')
    honeypot = StringField('', 
            [
                length_honeypot
            ])    