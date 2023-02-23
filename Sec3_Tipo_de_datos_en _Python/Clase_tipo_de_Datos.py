# Tipo de Variables
# tipo int
x = 10
print(type(x))
# tipo str
y = 'hola mi amor'
print(type(y))
# tipo float
m = 10.5
print(type(m))
# tipo bool
n = True
print(type(n))
n = False
print(type(n))

print(x, y)

# cadenas en python cadena(String)

miGrupoFavorito = "guns&roses" + " " + "the best band group"
print("mi grupo favorito es: " + miGrupoFavorito)

miGrupoFavorito1 = "guns&roses"
commentario = "the best band group"
print("mi grupo favorito es: " + miGrupoFavorito1 + " " + commentario)
print("mi grupo favorito es:", miGrupoFavorito1, commentario)
print(f"mi grupo favorito es {miGrupoFavorito1} ya que es {commentario}")

# mas temas de manejo de cadenas

numero1 = "1"
numero2 = "2"
print("concatenacion:", numero1 + numero2)
print("Suma", int(numero1) + int(numero2))

numero1 = 1
numero2 = 2
print(numero1 + numero2)

# Tipos bool (boolean)

miVariable = False
print(miVariable)

miVariable = 3 > 2
print(miVariable)

if miVariable:
   print("El resultado fue verdadero")
else:
   print("El resultado fue falso")

# Funcion input para procesar la entrada del usuario

resultado = input("Escribe un mensaje: ")
print("Valor proporcionado", resultado)
print("Fin del programa")

numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado1 = numero1 + numero2
print("Valor proporcionado", numero1, numero2)
print ("la suma de los valores 1 y 2 es: ", resultado1)
print("Fin del programa")

#ejercicio califica tu dia

valor = int(input("Como estuvo tu dia (1 al 10): "))
if valor > 10:
    print("Valor no es valido")
else:
    print("Mi dia estuvo de", valor)
print("Fin del programa")
