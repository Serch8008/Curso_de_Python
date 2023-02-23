def mi_funcion (nombre, apellido):
    print('saludos a la banda')
    print(f'Nombre:{nombre} Apellido: {apellido}')

mi_funcion('Sergio', 'avila')
mi_funcion('Karla', 'Lara')

# def sumar(a,b):
#     return (a + b)
# resultado = sumar(4,6)
# print(f'resultado de la suma {resultado}' )

def sumar(a,b):
    return (a + b)
print(f'resultado de la suma {sumar(4,6)}' )

def sumar(a=0,b=0):
    return (a + b)
print(f'resultado de la suma {sumar(8, 6)}' )

def lista_nombres(*nombres):
    for nombre in nombres:
        print(nombre)
lista_nombres('Juan','Pedro','Manuel', 'Ricardo')
lista_nombres('pedro', 'simon')

# def lista_numero(*args):
def lista_numero(*numeros):
    for numero in numeros:
        print(numero)
lista_nombres(1,2.5,6,'80',True)

# def listar_terminos(**kwargs):
def listar_terminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')
listar_terminos(IDE = 'integrated Frvrlopment environment', PK = 'Primary key')

def desplegar_nombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres = ['Sergio', 'Fabiola', 'Olga']
desplegar_nombres(nombres)
desplegar_nombres('esvetlana')
desplegar_nombres(('8', '9'))
desplegar_nombres(['10', '11'])

# Refactorizacion usando funciones recursivas
# 5! = 5*4*3*2*1
# 5! = 5*4*3*2
# 5! = 5*4*6
# 5! = 5*24
# 5! = 120

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)
numero = 3
result = factorial(numero)
print(f'el factorial de {numero} es {result}')



