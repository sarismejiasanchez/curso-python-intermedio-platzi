def run():
    
    #Diccionario cuyas llaves sean los 100 primeros numeros naturales y 
    #cuyos valores sean esos numeros elevados al cubo
    #my_dict = {}

    # for i in range(1, 101):
    #     my_dict[i] = i**3
    
    #Solo guardamos en el diccionario los números que no sean divisibles por 3
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3

    #Dictionary comprehensions
    # my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    # print(my_dict)

    #Reto
    #Dictionary comprehensions cuyas llaves sean los primeros 1000 numeros naturales y
    #cuyos valores sean la raíz cuadrada del mismo
    
    dict_sqrt = {i: pow(i, 0.5) for i in range(1, 1001)}
    print(dict_sqrt)

if __name__ == '__main__':
    run()