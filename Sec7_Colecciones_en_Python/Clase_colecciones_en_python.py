# --------definir una lista de tipo str ----------------#
# nombre = ["juan","pablo","pedro","jose","alma","Fabi"]
# #--------imprimir la lista nombre
# print(nombre)
# #--------acceder a los elementos de una lista
# print(nombre[0])
# print(nombre[1])
# #--------acceder a los elementos de manera inversa
# print(nombre[-1])
# print(nombre[-2])
# #--------imprimir un rango
# print(nombre[0:2])# sin incluir el indice 2 3 4
# #--------ir del inicio de la lista al indice(sin incluirlo)
# print(nombre[:3])
# #--------desde el indice indicado hasta el final
# print(nombre[1:])
# #--------cambiar un valor
# nombre [3] = 'Ivone'
# print(nombre)
# #--------iterar una lista
# for nom in nombre:
#     print(nombre)
# else:
#     print('no existen mas nombres en la listas')
# #--------preguntar el largo de una listas
# print(len(nombre))
# #--------agregegar un nuevo elemento
# nombre.append('sergio')
# print(nombre)
# #--------insertar un elemento en un indice en especifico
# nombre.insert(1,'Oracio')
# print(nombre)
# #--------remover un elemento
# nombre.remove('jose')
# print(nombre)
# #--------remover el ultimo valor agregado
# nombre.pop()
# print(nombre)
# #--------eliminar un indice
# del nombre [0]
# print(nombre)
# #--------limpiar lista
# nombre.clear()
# print(nombre)
# #--------borrar la lista por completo
# # del nombre
# # print(nombre)


#tuplas en python

#--------definir una tupla----------------#

# frutas = ("naranja","uva","platano","guayaba")
# print(frutas)
# #--------saber el largo
# print(len(frutas))
# #--------acceder a un elemento
# print(frutas[0])
# #--------navegacion inversa
# print(frutas[-1])
# #--------acceder a un rango de valores
# print(frutas[0:1]) #sin incluir el ultimo indice
# #--------recorrer elementos
# for fruta in frutas:
#     print(fruta, end=' ')
# #--------cambia valor tupla --- no es buena practica
# # frutas[0] = 'pera'
# fruta_lista = list(frutas)
# fruta_lista[0] = 'Pera'
# frutas = tuple(fruta_lista)
# print('\n',frutas)

#--------eliminar tupla
# del frutas
# print(frutas)


#----------------definir set ----------------#
# planetas = {'Marte', 'Jupiter','venus' }
# print([planetas])
# #----------------largo
# print(len(planetas))
# #----------------revisar si un elemento esta presente
# print('Marte' in planetas)
# #----------------agregar un elemento
# planetas.add('saturno')
# print(planetas)
# #----------------no se visualizan cuando se duplicar elementos
# planetas.add('Jupiter')
# print(planetas)
# #----------------eliminar elemento posiblemente arrojando un error
# planetas.remove('Jupiter')
# print(planetas)
# #----------------eliminar elemento sin arrojar error
# planetas.discard('venus')
# print(planetas)
# #----------------limpiar set
# planetas.clear()
# print(planetas)
#----------------eliminar set
# del planetas
# print(planetas)

#----------------Diccionarios (key: value)

diccionario = {
    'IDE':'integrated development environment',
    'OOP':'Object Oriented Programing',
    'DBMS':'Database Management System'
}
print(diccionario)
#----------------largo
print(len(diccionario))
#----------------acceder a un elemento
print(diccionario['IDE'])
#----------------otra forma de revcuperar un elemento
print(diccionario.get('OOP'))
#----------------modificando elementos
diccionario['IDE'] = 'Integrated Development Environment'
print(diccionario)

#----------------recorrer los elementos
for termino, valor in diccionario.items():
    print(termino, valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

#----------------comprobar exitencia de un elemento
print('IDE' in diccionario)

#----------------agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

#----------------remover un elemento
diccionario.pop('DBMS')
print(diccionario)

#----------------limpiar un diccionario
diccionario.clear()
print(diccionario)

#----------------eliminar un diccionario
del diccionario
print(diccionario)




