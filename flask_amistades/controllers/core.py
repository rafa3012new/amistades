#se importa el app
from unittest import result
from winreg import FlushKey
from wsgiref.util import request_uri
from flask_amistades import app
#se importa el modelo que contiene la clase
from flask_amistades.models.usuario import Usuario
from flask_amistades.models.amistad import Amistad
#se importa las funciones de flask
from flask import render_template, redirect, request, session, flash, jsonify
#se importan el modulo de fechas
from datetime import datetime


@app.route("/limpiar")
def limpiar():
   session.clear()
   print("se limpio la sesion",flush=True)
   return redirect("/")

#Funcion para obtener los registros de todos los dojos
# obtiene todos los dojos y las devuelve en una lista de objetos de los dojos
@app.route('/')
def home():
  data_usuarios = Usuario.get_all()
  data_amistades = Amistad.get_all_complete()
  return render_template('main_amistades.html',usuarios=data_usuarios, amistades=data_amistades)


# #Funcion para crear un dojo en la db con los datos que vienen de un formulario
# #Merodo Post para recibir los datos de un formulario o popupinput
@app.route('/crearusuario',methods=['POST'])
def crearusuario():

   data = {"nombre" : request.form['nombre'],
           "apellido" : request.form['apellido'],}

   resultado = Usuario.save(data)

   return redirect('/limpiar')


# #Funcion para crear un dojo en la db con los datos que vienen de un formulario
# #Merodo Post para recibir los datos de un formulario o popupinput
@app.route('/crearamistad',methods=['POST'])
def crearamistad():

   data = {"id_usuario" : request.form['usuario'],
           "id_amigo" :   request.form['amigo']}

   #Se valida si existe la amistad
   hayamistad = Amistad.validar_amistad(data)

   print(hayamistad,flush=True)
   #Se guarda la amistad
   if hayamistad == False:
      Amistad.save(data)
   else:
      print("no se establecio relacion de amistad, porque ya son amigos")

   return redirect('/limpiar')


# #Funcion para crear un dojo en la db con los datos que vienen de un formulario
# #Merodo Post para recibir los datos de un formulario o popupinput
@app.route('/eliminaramistad/<id_usuario>/<id_amigo>/')
def eliminaramistad(id_usuario,id_amigo):
   data = {"id_usuario" : int(id_usuario),
           "id_amigo" :   int(id_amigo)}

   print("antes de eliminar la amistad",flush=True)
   #Se valida si existe la amistad
   Amistad.delete(data)
   print("despues de eliminar la amistad",flush=True)
   return redirect('/limpiar')

