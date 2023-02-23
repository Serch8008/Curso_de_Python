# class Persona:
#     def __init__(self):
#         self.nombre = 'Juan'
#         self.apellido = 'Perez'
#         self.edad = '28'
#
# persona1 = Persona()
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)
# persona2 = Persona()
# print(persona2.nombre)
# print(persona2.apellido)
# print(persona2.edad)



# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#
# persona1 = Persona('Sergio', 'Avila', 42)
# # print(persona1.nombre)
# # print(persona1.apellido)
# # print(persona1.edad)
# print(f'objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')
# persona1.nombre = 'Juan carlos'
# persona1.apellido = 'aves'
# persona1.edad = 28
# print(f'objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')
#
# persona2 = Persona('Karla', 'Gomez', 30)
# print(f'objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')
# persona2.nombre = 'beto'
# persona2.apellido = 'boticario'
# persona2.edad = 35
# print(f'objeto persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')
#
# persona3 = Persona('Sergio', 'Avila', 42)
# print(f'objeto Persona 2: {persona3.nombre} {persona3.apellido} {persona3.edad}')



# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#
#     def mostrar_detalle(self):
#         print(f'Persona: {self.nombre} {self.apellido} {self.edad}')
#
# persona1 = Persona('Sergio', 'Avila', 42)
# persona1.mostrar_detalle()
#
# persona2 = Persona('Karla', 'Gomez', 30)
# persona2.mostrar_detalle()


# class Persona:
#     def __init__(this, nombre, apellido, edad):
#         this.nombre = nombre
#         this.apellido = apellido
#         this.edad = edad
#
#     def mostrar_detalle(self):
#         print(f'Persona: {self.nombre} {self.apellido} {self.edad}')
#
# persona1 = Persona('Sergio', 'Avila', 42)
# persona1.mostrar_detalle()
# # Persona.mostrar_detalle(persona1)
# persona1.telefono = '55361494'
# print(persona1.telefono)
#
# persona2 = Persona('Karla', 'Gomez', 30)
# persona2.mostrar_detalle()

# class Persona:
#     def __init__(self, nombre, apellido, edad, *valores, **terminos):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.valores = valores
#         self.terminos = terminos
#
#     def mostrar_detalle(self):
#         print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos} ')
#
# persona1 = Persona('Sergio', 'Avila', 42, '6946519151', 2, 3, 5, m='manzana', p='pera')
# persona1.mostrar_detalle()
#
# persona2 = Persona('Karla', 'Gomez', 30)
# persona2.mostrar_detalle()


# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self._nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#
#     def mostrar_detalle(self):
#         print(f'Persona: {self._nombre} {self.apellido} {self.edad}')
#
# persona1 = Persona('Sergio', 'Avila', 42)
# persona1._nombre = 'Juan C'
# persona1.mostrar_detalle()


class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    @property
    def nombre(self):
        print('llamando metodo get nombre')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print('llamando metodo set nombre')
        self._nombre = nombre

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')

persona1 = Persona('Sergio', 'Avila', 42)
# print(persona1.nombre)
#persona1.nombre = 'checo manuel'
print(persona1.nombre)
#
# # persona1._nombre = 'cambio'
# # print(persona1._nombre)

# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self._nombre = nombre
#         self._apellido = apellido
#         self._edad = edad
#
#     @property
#     def nombre(self):
#         return self._nombre
#
#     @nombre.setter
#     def nombre(self, nombre):
#         self._nombre = nombre
#
#     @property
#     def apellido(self):
#         return self._apellido
#
#     @apellido.setter
#     def apellido(self, apellido):
#         self._apellido = apellido
#
#     @property
#     def edad(self):
#         return self._edad
#
#     @edad.setter
#     def edad(self, edad):
#         self._edad = edad
#
#     def mostrar_detalle(self):
#         print(f'Persona: {self._nombre} {self._apellido} {self._edad}')
#
#     def __del__(self):
#         print(f'persona: {self._nombre} {self._apellido}')
#
# if __name__ == '__main__':
#     persona1 = Persona('Sergio', 'Avila', 42)
#     persona1.nombre = 'checo manuel'
#     persona1.apellido = 'avila'
#     persona1.edad = 40
#     persona1.mostrar_detalle()
#
#     print(__name__)
#
#
#
#
#
