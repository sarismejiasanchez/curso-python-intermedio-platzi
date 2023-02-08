def run():
    #Funcion de Orden Superior
    #Es una función que recibe como parámetro a otra función

    #Filter
    #Quiero obtener una lista de sólo los números que son impares.
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]
    odd = list(filter(lambda x: x%2 != 0, my_list))
    #Resultado: [1, 5, 9, 13, 19, 21]
    print("Filter", odd)


    #Map
    #Quiero obtener los valores de mi lista inicial, elevados al cuadrado
    my_list = [1, 2, 3, 4, 5]
    odd = list(map(lambda x: x**2, my_list))
    #Resultado: [1, 4, 9, 16, 25]
    print("Map", odd)

    #Reduce
    #Reduciendo los valores de la lista a un único valor
    from functools import reduce
    my_list = [2, 2, 2, 2, 2]
    all_multiplied = reduce(lambda a, b: a * b, my_list)
    #Resultado: 32
    print("Reduce", all_multiplied)

if __name__ == '__main__':
    run()