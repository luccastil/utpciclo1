# ACA SOLO VA LA PARTE LOGICA, LO QUE INTERACTUE CON EL USUARIO SE VA
# Los import siempre en la cabecera del archivo
# Siempre ir probando de a poco el codigo
# Para trabajar con json, debemos importar una biblioteca para poder interactuar con el import json

import json

# Funcion para crear una tarea


def create(tareas: dict, clave: str, valor: dict) -> dict:
    # No hacemos validacion, por lo tanto, me sobreescribe la tarea 2 siempre
    # TAREA: Validacion de que la llave exista para que no se sobreescriba
    tareas[clave] = valor
    return tareas

# Funcion para leer las tareas -> Muestra informacion entonces va a la vista
# Crearemos una nueva funcion read. Va ser el puente entre el json y la vista


def read():
    datos = {}
    # try except nos permite decirle al programa como se comporte si hay un error
    try:
        with open("modelo.json") as archivo:
            # archivo sera la variable donde almacenamos el json referenciado
            datos = json.load(archivo)
    except:
        datos = {}
        print("Error al cargar el archivo JSON")

    return datos

# Funcion para actualizar una tarea


def update(tareas: dict, clave: str, nuevoValor: dict) -> dict:
    claves = tareas.keys()
    if clave in claves:
        tareas[clave] = nuevoValor

    return tareas

# Funcion para eliminar una tarea


def delete(tareas: dict, llave: str):
    # Obtiene todas las llaves dle diccionario
    claves = tareas.keys()
    if llave in claves:
        # Elimina el item del diccionario
        # Con la llave especificada
        tareas.pop(llave)
    # Retorna de nuevo el diccionario
    return tareas

# Funcion para guardar las tareas


def save(tareas: dict) -> bool:
    # Usamos try except por si las moscas
    # Creamos una variable vacia para que: True si guardo los cambios y False si sucedio un error al sobreescribir el fichero
    resp: bool = None
    try:
        # Vamos a abrir el archivo con permiso de escritura, eso es la "w"
        with open("modelo.json", "w") as archivo:
            # Las tareas las vamos a guardar en modelo.json
            # Si se pone otro nombre, crea otro archivo nuevo con ese nombre
            json.dump(tareas, archivo)
            resp = True
    except:
        resp = False
    return resp

# menu se va a vista porque se muestra al usuario


# Probar si read funciona:
# print(read())
