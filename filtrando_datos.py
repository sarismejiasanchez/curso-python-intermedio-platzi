# Cuando colocamos el nombre de una variable en mayuscula, quiere decir que en el futuro
# no esperamos modificarla y en lugar de variable, deberíamos de llamarle CONSTANTE

#lista de diferentes diccionarios
from ast import comprehension


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'HÃ©ctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    #Filtros

    #Nombre de todos los trabajadores de python
    #Usando list comprehensions
    #worker = cada uno de los diccionarios internos de DATA
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]

    #RETO
    #Usando filter y map
    all_python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))

    #Nombre de todos los trabajadores de Platzi
    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]

    #RETO
    #Usando filter y map
    all_Platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_Platzi_workers = list(map(lambda worker: worker["name"], all_Platzi_workers))

    #Nombre de todos los adultos, usando Filter
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    
    #Creamos adults a partir de la variable anterior
    #aplicando map sobre cada uno de los diccionarios que contiene
    #extrayendo el valor de la variable nombre
    adults = list(map(lambda worker: worker["name"], adults))

    #RETO
    #Usando list comprehensions
    adults = [worker["name"] for worker in DATA if worker["age"] > 18]

    #Crear una nueva lista de diccionarios, pero
    #en lugar de tener las llaves que ya conociamos
    #tengamos una llave más, una llave "old"
    #que va a tener un valor True o False dependiendo si es mayor a 70 años o menor
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    #RETO
    #Usando list comprehensions
    old_people = [worker | {"old" : worker["age"] > 70} for worker in DATA]

    for worker in old_people:
        print(worker)

if __name__ == '__main__':
    run()