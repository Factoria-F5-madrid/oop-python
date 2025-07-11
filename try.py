
# 1.  Impresora sin inyección y sin abstracción, imprime solo con tipo de papel que dice la clase. Acoplamiendo fuerte

class GlossyPaper:
      def description(self):
            return "Glossy paper"

class Printer:
      def __init__(self):
            self.paper = GlossyPaper()    # La impresora crea su propio papel (acoplamiento fuerte)

      def print_document(self, document: str):
            print(f"Printing on {self.paper.description()}: {document}")

printer = Printer()
printer.print_document("Hello, world!")










# 2. Impresora con inyección de dependencias, imprime con tipo de papel que se le pasa

class SimplePaper:
      def description(self):
            return "Paper Simple"

class MattePaper:
    def description(self):
        return "Papel mate"
      
class Printer:
      def __init__(self, paper): 
            self.paper = paper
            
      def print_document(self, document):
            print(f"Printing on {self.paper.description()}: {document}")
            
simple = Printer(SimplePaper())
simple.print_document("Hello, world!")

matte = Printer(MattePaper())
matte.print_document("Hello, world!")

#3. Impresora con abstracción e inyección, imprime con tipo de papel que se le pasa. Además inversión de dependencias, la clase grande depende de una clase abstracta.

from abc import ABC, abstractmethod

class PaperType(ABC):
    @abstractmethod
    def descripcion(self):
        pass

class GlossyPaper(PaperType):
    def descripcion(self):
        return "Papel brillante"

class MattePaper(PaperType):
    def descripcion(self):
        return "Papel mate"

class Printer:
    def __init__(self, paper_type: PaperType):
        self.paper_type = paper_type

    def print_document(self, document):
        print(f"Imprimiendo en {self.paper_type.descripcion()}: {document}")

# Inyección de dependencias
printer1 = Printer(GlossyPaper())
printer2 = Printer(MattePaper())

printer1.print_document("Factura 006")
printer2.print_document("Factura 007")
            







# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner  # Público
#         self._balance = balance  # Protegido (convención)
#         self.__password = "secure"  # Privado

#     def get_balance(self):
#         return self._balance

# # Creación de cuenta
# account = BankAccount("Bob", 1000)

# print(account.owner)  # ✅ Público
# print(account._balance)  # ⚠️ Protegido, pero accesible
# # print(account.__password)  # ❌ AttributeError
# print(account._BankAccount__password)  # 🔥 Name Mangling (Evitar su uso)






# class Persona:
#     """
#     Clase que representa a una persona.

#     Atributos:
#         nombre (str): El nombre de la persona.
#         edad (int): La edad de la persona.
#     """
#     def __init__(self, nombre, edad):
#         """
#         Inicializa una nueva persona.

#         Args:
#             nombre (str): El nombre de la persona.
#             edad (int): La edad de la persona.
#         """
#         self.nombre = nombre
#         self.edad = edad

#     def saludar(self):
#         """
#         Método que imprime un saludo.
#         """
#         print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")


# persona = Persona("Juan", 30)
# persona2 = Persona("Ana", 30)




# persona.saludar()
# persona2.saludar()

# persona2.edad = 25
# persona2.saludar()

# print(persona.nombre)

# help(Persona)




















# class Person: #Los nombres de las clases de Python se escriben en notación CapitalizedWords por convención. 
#   def __init__(self, name, age): #__init__ es el constructor, la función especial que se ejecuta al crear una instancia de la clase. self es arbitraria, se puede llamar como se quiera. Es el primero
#     self.name = name # Atributo de instancia
#     self.age = age # Atributo de instancia

#   def introduce(self): #self es la referencia al objeto actual y permite acceder a sus atributos y métodos.
#     return f"Hello, I am {self.name} and I am {self.age} years old."

# # puedo añadir algo dinamicamente al objeto

# person = Person("John", 30)
# print(person.introduce())

# person.height = 1.75
# print(person.height)
# person.name = "Juan"
# print(person.name)




# from typing import final

# @final
# class Vehiculo:
#     pass

# class Coche(Vehiculo):  # ❌ ERROR: No se puede heredar de una clase final
#     pass

# print(Coche.__bases__ )


## EJEMPLOS DE PATRONES DE DISEÑO EN DJANGO

# #Clase.
# class Person:
#       def __init__(self, name, age):
#           self.name = name
#           self.age = age

# #Clase en Django
# from django.db import models
# class Persona(models.Model):
#       nombre = models.CharField(max_length=100)
#       edad = models.IntegerField()

#Encapsulamiento, las clases de los modelos

# #Composición y asociación
#   class Engine(models.Model):
#       tipo = models.CharField(max_length=50)
#   class Car(models.Model):
#       engine = models.ForeignKey(Engine, on_delete=models.CASCADE)

#En el setting, inyectas dependencias, en este caso el JWTAuthentication
# REST_FRAMEWORK = {
#       'DEFAULT_AUTHENTICATION_CLASSES': [
#           'rest_framework_simplejwt.authentication.JWTAuthentication',
#       ],
#   }