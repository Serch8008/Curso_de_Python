#ciclo while en python

# condicion = True
#
# while condicion:
#     print('Ejecutando ciclo while')
# else:
#     print('fin del ciclo while')

# contador = 0
#
# while contador < 4:
#     print(contador)
#     contador += 1 # contador = contador + 1
# else:
#     print('fin ciclo while')

# Ciclo for en python

# cadena = 'Sergio'
# for letra in cadena:
#     print(letra)
# else:
#     print('fin ciclo for')


# Palabra break en python

# for letra in 'holanda':
#     if letra == 'a':
#         print(f'letra encontrada {letra}')
#         break
# else:
#     print('fin del ciclo for')


# palabra continue

# for i in range(6):
#     if i % 2 == 0:
#         print(f'valor {i}')


for i in range(6):
    if i % 2 != 0:
        continue
    print(f'valor {i}')
