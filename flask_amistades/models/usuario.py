from flask_amistades.config.mysqlconnection import connectToMySQL
from flask_amistades.models import amistad

BASE_DATOS="amistades_dojo"

# modelar la clase después de la tabla usuarioscr de nuestra base de datos
class Usuario:
    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.amistades = []

    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL(BASE_DATOS).query_db(query)
        # crear una lista vacía para agregar nuestras instancias de usuarioscr
        usuarios = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for usuario in results:
            usuarios.append( cls(usuario) )
        return usuarios

    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_by_id(cls,id):
        #armar la consulta con cadenas f
        query = "SELECT * FROM usuarios where id = %(id)s;"
        #armar el diccionario data con solo el campo id
        data = { 'id' : id }
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL(BASE_DATOS).query_db(query, data)
        #devolver el primerl registro de los resultados si resultados devuelve algo sino que devuelva None
        return cls(results[0]) if len(results) > 0 else None

    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre , apellido) VALUES ( %(nombre)s , %(apellido)s);"
        print(query,flush=True)
        # data es un diccionario que se pasará al método de guardar desde server.py
        id_usuario = connectToMySQL(BASE_DATOS).query_db( query, data )
        print(id_usuario,flush=True)
        return id_usuario



    @classmethod
    def update(cls, data):
        query =  "UPDATE usuarios SET nombre = %(nombre)s , apellido = %(apellido)s WHERE id = %(id)s;"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL(BASE_DATOS).query_db( query, data )


    @classmethod
    def delete(cls, id):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        data = {'id': id}

        print("ejecutando consulta de borrado",end='\n\n')
        print(query)

        resultado = connectToMySQL(BASE_DATOS).query_db(query, data)

        return resultado