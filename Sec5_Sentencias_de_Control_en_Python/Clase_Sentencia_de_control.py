#--------------------Sentencia If Else en Python

# condicion = 10
#
# if condicion == True:
#     print('condicion verdadera')
# elif condicion == False:
#     print('Condicion falsa')
# else:
#     print('Condicion no reconocida')


# --------------------Ejercicio Conversion de Numero a texto en Python

# numero = int(input('Proporciona un valor entre 1 y 3: '))
# numero_texto = ''
# if numero == 1:
#     numero_texto = 'Numero uno'
# elif numero == 2:
#     numero_texto = 'Numero dos'
# elif numero == 3:
#     numero_texto = 'Numero tres'
# else:
#     numero_texto = 'Valor fuera de rango'
# print(f'Numero proporcionado: {numero} - {numero_texto}')

# --------------------Sintesis if else simplificada

# condicion = True

# if condicion == True:
#     print('condicion verdadera')
# elif condicion == False:
#     print('Condicion falsa')
# else:
#     print('Condicion no reconocida')

# print('Condicion verdadera') if condicion else print('Condicion falsa')


# --------------------Sintesis if else simplificada

# mes = int(input('Proporciona mes del ano (1 al 12): '))
# estacion = None
# if mes == 1 or mes == 2 or mes == 12:
#     estacion = 'Invierno'
# elif mes == 3 or mes == 4 or mes == 5:
#     estacion = 'primavera'
# elif mes == 6 or mes == 7 or mes == 8:
#     estacion = 'verano'
# elif mes == 9 or mes == 10 or mes == 11:
#     estacion = 'otonio'
# else:
#     estacion = 'Mes incorrecto'
# print(f'Para el mes {mes} la estacion es {estacion}')

# --------------------Ejercicio Etapas de la vida segun la edad
# mi solucion
# edad = int(input('Proporciona tu edad: '))
#
# if edad >=0 and edad <= 10:
#     print('la infancia es increible')
# elif edad >=11 and edad <= 20:
#     print('Muchos cambios y mucho estudio')
# elif edad >=21 and edad <= 30:
#     print('Amor y comienza el trabajo')
# else:
#     print('Ya estas betabel')

edad = int(input('Proporciona tu edad: '))
mensaje = ''

if 0 <= edad < 10:
    mensaje = 'la infancia es increible'
elif 10 <= edad < 20:
    mensaje = 'Muchos cambios y mucho estudio'
elif 20 <= edad < 30:
    mensaje ='Amor y comienza el trabajo'
else:
    mensaje = 'Ta estas viejito'

print(f'Tu edad es: {edad} , {mensaje}')





