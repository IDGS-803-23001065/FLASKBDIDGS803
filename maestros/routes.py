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
	create_form=forms.MaestroForm(request.form)
	if request.method == 'POST':
		maes=Maestros(nombre=create_form.nombre.data,
			   		 apellidos=create_form.apellidos.data,
				     email=create_form.email.data,
					 especialidad=create_form.especialidad.data
		)
		db.session.add(maes)
		db.session.commit()
		return redirect(url_for('maestros.index'))
	return render_template("maestros/maestros.html", form=create_form)

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

@maestros.route("/modificarMaes", methods=['GET', 'POST'])
def modificar():
    create_form = forms.MaestroForm(request.form)

    if request.method == 'GET':
        matricula = request.args.get('matricula')
        maes1 = Maestros.query.get(matricula)

        create_form.matricula.data = maes1.matricula
        create_form.nombre.data = maes1.nombre
        create_form.apellidos.data = maes1.apellidos
        create_form.email.data = maes1.email
        create_form.especialidad.data = maes1.especialidad

    if request.method == 'POST':
        matricula = request.form.get('matricula')
        maes1 = Maestros.query.get(matricula)

        maes1.nombre = create_form.nombre.data
        maes1.apellidos = create_form.apellidos.data
        maes1.email = create_form.email.data
        maes1.especialidad = create_form.especialidad.data

        db.session.commit()
        return redirect(url_for('maestros.index'))

    return render_template("maestros/modificarMaes.html", form=create_form)

@maestros.route("/eliminarMaes", methods=['GET', 'POST'])
def eliminar():
	create_form=forms.MaestroForm(request.form)
	if request.method=='GET':
		matricula=request.args.get('matricula')
		maes1=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		create_form.matricula.data=request.args.get('matricula')
		create_form.nombre.data=maes1.nombre
		create_form.apellidos.data=maes1.apellidos
		create_form.email.data=maes1.email
		create_form.especialidad.data=maes1.especialidad
	if request.method=='POST':
		matricula=request.args.get('matricula')
		maes1=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		create_form.matricula.data=request.args.get('matricula')
		create_form.nombre.data=maes1.nombre
		create_form.apellidos.data=maes1.apellidos
		create_form.email.data=maes1.email
		create_form.especialidad.data=maes1.especialidad
		db.session.delete(maes1)
		db.session.commit()
		return redirect(url_for('maestros.index'))
	return render_template("maestros/eliminarMaes.html", form=create_form)
