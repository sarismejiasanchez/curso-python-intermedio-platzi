#Recibir un número como parámetro y retornar una lista con todos los divisores de ese número
def divisors(num):
    divisors = []
    #Ciclo for
    for i in range(1, num + 1):
        if num % i == 1:
            divisors.append(i)
    return divisors

    #List comprehensions
    #pass
    
def run():
    num = int(input("Ingresa un número: "))
    print(divisors(num))
    print("Terminó mi programa")

if __name__ == '__main__':
    run()