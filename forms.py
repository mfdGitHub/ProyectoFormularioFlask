#from wtforms import Form 
from wtforms import Form 
from wtforms import StringField
from wtforms.fields import EmailField

class ComentForm(Form):
    username = StringField('username')
    email = EmailField('Correo electronico')
    comment = StringField('Comentario')
    