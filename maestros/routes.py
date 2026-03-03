from . import maestros
from flask import render_template, request, redirect, url_for
from models import db
from models import Maestros
from flask_wtf import FlaskForm
import forms

@maestros.route('/perfil/<nombre>')
def perfil():
    return f"perfil de"

@maestros.route("/maestros_crear", methods=['GET', 'POST'])
def crear_maestros():
	create_form=forms.UserForm(request.form)
	if request.method == 'POST':
		maes=Maestros(nombre=create_form.nombre.data,
			   		 apellidos=create_form.apellidos.data,
				     email=create_form.email.data,
					 especialidad=create_form.especialidad.data
		)
		db.session.add(maes)
		db.session.commit()
		return redirect(url_for('perfil'))
	return render_template("usuarios/registrar.html", form=create_form)

@maestros.route("/maestros", methods=['GET', 'POST'])
def index():
	create_form=forms.MaestroForm(request.form)
	maestro=Maestros.query.all()
	return render_template("maestros/listado.html", form=create_form,maestro=maestro)

@maestros.route("/detallesMaes", methods=['GET', 'POST'])
def detalles():
	if request.method=='GET':
		matricula=request.args.get('matricula')
		maes1=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		matricula=request.args.get('matricula')
		nombre=maes1.nombre
		apellidos=maes1.apellidos
		especialidad=maes1.especialidad
		email=maes1.email
		return render_template("maestros/detalleMaes.html", nombre=nombre,
						 apellidos=apellidos, email=email, especialidad=especialidad)
