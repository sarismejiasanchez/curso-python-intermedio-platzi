def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firtname": "Sara", "lastname": "Mejia"}

    #Lista que contiene diccionarios
    super_list = [
        {"firtname": "Sara", "lastname": "Mejia"},
        {"firtname": "Facundo", "lastname": "Garcia"},
        {"firtname": "Miguel", "lastname": "Torres"},
        {"firtname": "Pepe", "lastname": "Rodelo"},
        {"firtname": "Susana", "lastname": "Martinez"},
        {"firtname": "Jose", "lastname": "Jose"}
    ]

    #diccionario de listas
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.42]
    }

    #permite recorrer las llaves y valores de un diccionario en un ciclo
    for key, value in super_dict.items():
        print(key, " - ", value)

#Iniciar la funcion cuando ejecutamos el archivo de python
if __name__ == '__main__':
    run()