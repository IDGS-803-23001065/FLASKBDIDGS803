from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    id=IntegerField('id')
    nombre=StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4,max=10,message="Ingresa nombre valido")
    ])
    apellidos=StringField('Apellidos',[
        validators.DataRequired(message="El campo es requerido"),

    ])
    email=EmailField('Correo',[
        validators.email(message="Ingrese un correo valido"),
    ])
    telefono = StringField('Telefono', [
    validators.DataRequired(message="El telefono es requerido")
    ])

class MaestroForm(Form):
    matricula=IntegerField('matricula')
    nombre=StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4,max=10,message="Ingresa nombre valido")
    ])
    apellidos=StringField('Apellidos',[
        validators.DataRequired(message="El campo es requerido"),

    ])
    email=EmailField('Correo',[
        validators.email(message="Ingrese un correo valido"),
    ])
    especialidad = StringField('Especialidad', [
    validators.DataRequired(message="La especialidad es requerida")
    ])
