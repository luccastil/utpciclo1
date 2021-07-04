# SOLO DEJAMOS LO QUE INTERACTUA CON EL USUARIO
# Debemos importar el controlador para acceder a las funciones, para acceder a ellas sera controlador.funcion

import controlador

# Leer las tareas


def show(tareas: dict):
    for clave, tarea in tareas.items():
        print("------------------------")
        print(clave, ": ")
        for llave, valor in tarea.items():
            print(llave, " - ", end=' ')
            print(valor)
        print("------------------------")

# Funcion que me representa el menu
# UI (User Interface)


def menu():
    # El Diccionario inicial ahora debe ser el del json, estos estan en read del controlador
    tareas = controlador.read()
    # Vamos a cambiar el autoincrementable para que no sobreescriba en la ultima tarea
    # Vamos a obtener y castear las llaves de tareas a enteros
    keys = list(map(int, tareas.keys()))
    # Cuando se cree una, se suma uno y asi no se sobreescriba
    aut: int = max(keys) + 1
    opc: int = -1
    while opc != 0:
        # Pedir los datos (inputs)
        print(">>>-----Gestor de tareas------<<<")
        print("")
        print("1 -> Crear tarea")
        print("2 -> Consultar todas las tareas")
        print("3 -> Actualizar una tarea")
        print("4 -> Eliminar una tarea")
        print("5 -> Guardar todos los cambios")
        print("0 -> Salir")
        print("")
        # Solicitar datos al usuario
        opc = int(input("Por favor ingrese una opción>>> "))
        # Llama las funcionalidades según su opción
        if opc == 1:
            desc: str = input("Descripción de la tarea: ")
            est: str = input("Estado de la tarea: ")
            tiempo: int = int(input("Tiempo de ejecución de la tarea: "))
            # Crea el diccionario con los valores del usuario
            val_diccionario = {
                'descripcion': desc,
                'estado': est,
                'tiempo': tiempo
            }
            tareas = controlador.create(tareas, '0'+str(aut), val_diccionario)
            aut += 1
            print("--------------------------")
            print("\t¡Tarea creada con éxito!")
            print("--------------------------")
        elif opc == 2:
            show(tareas)
        elif opc == 3:
            clave: str = input("Por favor ingrese el id de la tarea: ")
            claves = tareas.keys()
            if clave in claves:
                desc: str = input(
                    "Nueva descripción de la tarea a actualizar: ")
                est: str = input("Nuevo estado de la tarea: ")
                tiempo: int = int(
                    input("Nuevo tiempo de ejecución de la tarea: "))
                val_diccionario = {
                    'descripcion': desc,
                    'estado': est,
                    'tiempo': tiempo
                }
                tareas = controlador.update(tareas, clave, val_diccionario)
                print("------------------------------------------")
                print("\t¡Tarea actualizada con éxito!")
                print("------------------------------------------")
            else:
                print("------------------------------------------")
                print("\tLa tarea ingresada no existe")
                print("------------------------------------------")
                input("Enter para continuar >>> ")
                continue
        elif opc == 4:
            # Al manipular aca, no me elimina en el modelo, sino en la memoria, vamos a crear otra opcion para modificar el modelo, va al controlador
            clave: str = input(
                "Por favor ingrese el id de la tarea a eliminar: ")
            claves = tareas.keys()
            if clave in claves:
                tareas = controlador.delete(tareas, clave)
            else:
                print("------------------------------------------")
                print("La tarea ingresada no existe")
                print("------------------------------------------")
                input("Enter para continuar >>> ")
                continue
        elif opc == 5:
            resp = controlador.save(tareas)
            if resp:
                print("------------------------------------------")
                print("¡Cambios guardados con éxito!")
                print("------------------------------------------")
            else:
                print("------------------------------------------")
                print("Ups! Algo sucedio, intenta mas tarde")
                print("------------------------------------------")

    # return


# Llama la función principal
menu()
