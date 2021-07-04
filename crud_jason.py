'''Modelo Vista - Controlador'''
# Es que podamos cerrar el programa y la informacion se guarde para futuras consultas
# Se debe seguir separando la vista y la parte logica
# M -> Modelo de datos -> CRUD DE TAREAS: serian las tareas. El modelo tiene una descripcion, un estado y un tiempo en un diccionario.
# V -> La parte que interactua con el usuario UI.
# C -> Lo que me hace puente entre el modelo de datos y la UI. Es la LOGICA Por ejemplo, cuando en la vista pido un dato,
# se lo solicito al controlador. Este los obtiene, los transforma y se los entrega a la vista.
# El flujo seria V->C->M

'''JSON'''
# Es como un diccionario gigante

'''Construccion'''
# Vamos a tener las tres por separado
# Usualmente se hace el controlador y sobre el, cuando ya se pobro, se construye lo demas
