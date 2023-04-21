#la idea de esta clase es poder grabar las friendships
from flask_amistades.config.mysqlconnection import connectToMySQL
from flask_amistades.models import usuario

BASE_DATOS="amistades_dojo"

# modelar la clase después de la tabla friendships de nuestra base de datos
class Amistad:
    def __init__( self , data ):
        self.id_usuario= data['id_usuario']
        self.id_amigo = data['id_amigo']
        self.nombre_usuario = data['nombre_usuario']
        self.nombre_amigo = data['nombre_amigo']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM amistades;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL(BASE_DATOS).query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friendships
        amistades = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friendships con cls
        for amistad in results:
            amistades.append( cls(amistad) )
        return amistades
    
        # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all_complete(cls):

        query = 'select a.id_usuario, a.id_amigo, CONCAT(u1.nombre, " ", u1.apellido) as nombre_usuario, CONCAT(u2.nombre, " ", u2.apellido) as nombre_amigo, a.created_at, a.updated_at from amistades a left join usuarios u1 on a.id_usuario = u1.id left join usuarios u2 on a.id_amigo = u2.id;'
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL(BASE_DATOS).query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friendships
        amistades = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friendships con cls
        for amistad in results:
            amistades.append( cls(amistad) )
        return amistades

    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_by_id(cls,id_usuario,id_amigo):
        #armar la consulta con cadenas f
        query = 'SELECT * FROM amistades where id_usuario = %(id_usuario)s and id_amigo = %(id_amigo)s;'
        #armar el diccionario data con solo los campos user_id y friend_id
        data = {
                'id_usuario' : id_usuario ,
                'id_amigo' : id_amigo
                }
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL(BASE_DATOS).query_db(query, data)
        #devolver el primerl registro de los resultados si resultados devuelve algo sino que devuelva None
        return cls(results[0]) if len(results) > 0 else None

    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def validar_amistad(cls,data):
        #se inicializa las vaiables
        condicion = False
        results = []
        #armar la consulta con cadenas f
        query = 'select count(*) as hayamistad from amistades where (id_usuario = %(id_usuario)s and id_amigo = %(id_amigo)s);'

        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL(BASE_DATOS).query_db(query, data)

        valor1 = results[0]['hayamistad']
        
        print("valor 1 : ",valor1,flush=True)

        #armar la consulta con cadenas f
        query = 'select count(*) as hayamistad from amistades where (id_usuario = %(id_amigo)s and id_amigo = %(id_usuario)s);'

        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL(BASE_DATOS).query_db(query, data)

        valor2 = results[0]['hayamistad']

        print("valor 2 : ",valor2,flush=True)

        results = []

        condicion = valor1 > 0 or valor2 > 0

        return condicion

    @classmethod
    def save(cls, data):
        query = "INSERT INTO amistades (id_usuario , id_amigo ) VALUES ( %(id_usuario)s, %(id_amigo)s );"
        # data es un diccionario que se pasará al método de guardar desde server.py
        print('antes',flush=True)
        friend_id = connectToMySQL(BASE_DATOS).query_db( query, data )
        print('despues',flush=True)
        return data


    @classmethod
    def delete(cls, data):
        query = "DELETE FROM amistades WHERE id_usuario = %(id_usuario)s and id_amigo = %(id_amigo)s;"
        print(query,flush=True)
        resultado = connectToMySQL(BASE_DATOS).query_db(query, data)

        return resultado
