#Son inmutables: No se pueden modificar
#Metodos que no son compatibles con tuplas: remove(), insert(), append(), pop(), sort()
#Metodos para tuplas: index(), count()
#Para modificar una tupla debe convertirla a la lista
#Son indexadas

Tuplas = () #Tupla vacia
Días_semana = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Lunes", "Lunes", "Domingo", "Domingo")

#Acceder a elemento de la tupla:
print(Días_semana[3])
print(Días_semana[-3]) #Ingresa la tupla de forma inversa.

#Conocer cuantas veces se repite un elemento (moda): count()
print(Días_semana.count("Sabado"))

#Conocer la posición de un elemento: index()
print(Días_semana.index("Jueves"))

#Modificar tupla: debe convertirla a lista
Días_semana = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Lunes", "Lunes", "Domingo", "Domingo")
lista = list(Días_semana)
print(type(lista))
print(lista)
lista.append("Sabado")
print(lista)

#Las tuplas también se pueden representar de esta manera
tupla1 = 1, 2, 3, 4, 5
tupla3 = 6