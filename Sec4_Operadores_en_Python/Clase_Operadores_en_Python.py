#operadores aritmeticos
'''
operadorA = 5
operadorB = 4

#print('El resultado es', suma)
int('El resultado es', resta)
resta = operadorA - operadorB
print(f'Resultado resta es: {resta}')
#print('El resultado es', multiplicacion)
multiplicacion = operadorA * operadorB
print(f'Resultado multiplicacion es: {multiplicacion}')
#print('El resultado es', division)
division = operadorA / operadorB
print(f'Resultado division es: {division}')
#print('El resultado es', suma)
division = operadorA // operadorB
print(f'Resultado division int es: {division}')
#print('El resultado es', suma)
modulo = operadorA % operadorB
print(f'Resultado del residuo division u operador Modulo {modulo}')
exponente = operadorA ** operadorB
print(f'Resultado exponente: {exponente}')
operacion = operadorA + operadorB * operadorA / operadorB ** operadorA
print(f'Resultado de la operacion es: {operacion}')'''

#operadores de asignacion

'''miVariable = 10
print(miVariable)
miVariable = miVariable + 1
print(miVariable)
############## Incremento con reasignacion
miVariable += 1
print(miVariable)
# miVariable = miVariable - 2
miVariable -= 2
print(miVariable)
# miVariable = miVariable * 3
miVariable *= 3
print(miVariable)
# miVariable = miVariable / 2
miVariable /= 2
print(miVariable)'''


#operadores de comparacion

'''a = 4
b = 2

resultado = a == b
print(f'resultado es ==: {resultado}')
resultado = a != b
print(f'resultado es !=: {resultado}')
resultado = a > b
print(f'resultado es >: {resultado}')
resultado = a >= b
print(f'resultado es >=: {resultado}')
resultado = a < b
print(f'resultado es <: {resultado}')
resultado = a <= b
print(f'resultado es <=: {resultado}')'''

#ejercicio numero para o impar

'''a = int(input('Escribe un valor numerico '))
# print(a % 2)
if a % 2 == 0:
    print(f'El valor de a {a} es numero par')
else:
    print(f'El valor de a {a} es numero impar')'''

#Ejercicio determina si es mayor de edad

'''edad_adulto = 18
edad_persona = int(input('Proporciona tu edad: '))

if edad_persona >= edad_adulto:
    print(f'la persona con edad {edad_persona} es mayor de edad')
else:
    print(f'la persona con edad {edad_persona} es menor de edad ')'''

#operadores Logicos
'''
a = True
b = False

resultdo = a and b
print(resultdo)

resultdo = a or b
print(resultdo)

resultdo = not a
print(resultdo)'''

# ejercicio Operador 'and' valor dentro de rango
'''valor = int(input('Escribe el valor: '))
valor_minimo = 0
valor_maximo = 5

dentro_rango = (valor >= valor_minimo) and (valor <= valor_maximo)

if dentro_rango:
    print(f'El valor {valor} esta dentro de rango')
else:
    print(f'El valor {valor} esta fuera de rango')'''

# ejercicio Operador 'or'

'''vacaciones = True
dia_descanso = True

if vacaciones or dia_descanso:
    print('Puede asistir al juego')
else:
    print('tiene deberes por hacer')'''

# ejercicio Operador 'not'

'''vacaciones = False
dia_descanso = False

if not (vacaciones or dia_descanso):
    print('tiene deberes por hacer')
else:
    print('Puede asistir al juego')'''

#Ejercicio rango entre 20's y 40's

'''edad = int(input('Introduce tu edad: '))

veintes = edad >= 20 and edad < 30
print(veintes)
trintas = edad >= 30 and edad < 40
print(trintas)

if veintes or trintas:
#    print('Dentro de rango 20\'s o 30\'s')
    if veintes:
        print('Dentro de los 20\'s')
    elif trintas:
        print('Dentro de los 30\'s')
    else:
        print('Fuera de rango')
else:
    print("No esta dentro de los 20's o 30's")'''

# otra manera mas reducida

'''edad = int(input('Introduce tu edad: '))

if (edad >= 20 and edad < 30) or (edad >= 30 and edad < 40):
    print('Dentro de rango 20\'s o 30\'s')
else:
    print("No esta dentro de los 20's o 30's")'''

#Ejercicio tienda de libros

print('proporciona los siguientes datos del libro')
nombre_del_libro = input('Proporciona el nombre del libro: ')
id_libro = int(input('proporciona el id: '))
precio_libro = float(input('Proporciona el precio: '))
envio_gratuito = input('Indica si el envio es gratuito (True / False): ')

if envio_gratuito == 'True' or 'true':
    envio_gratuito = True
elif envio_gratuito == 'False' or 'false':
    envio_gratuito = False
else:
    envio_gratuito = 'valor incorrecto debe escribir True / False'


print(f'''
    nombre: {nombre_del_libro}
    id:{id_libro}
    Precio: {precio_libro}
    envio gratuito: {envio_gratuito}
''')



