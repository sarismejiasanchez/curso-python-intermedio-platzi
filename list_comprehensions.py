def run():
    # squares = []
    
    # for i in range(1, 101):
    #     #Lista de los primeros 100 números naturales elevados al cuadrado
    #     squares.append(i**2)

    #     #Lista de los primeros 100 nmeros naturales elevados al cuadrado que no sean divisibles entre 3
    #     if i % 3 != 0:
    #         squares.append(i**2)
    
    #List comprehensions
    #squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    
    #print(squares)
    
    #Reto
    #Lista de todos los múltiplos de 4, que a la vez son múltiplos de 6 y de 9, hasta 5 digitos

    #multiplos = [i for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    multiplos = [i for i in range(1, 100000) if i % 36 == 0]
    print(multiplos)
    

if __name__ == '__main__':
    run()
