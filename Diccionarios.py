#Son mutables

diccionario = {}
Dicc1 = {"clave": "valor", "clave": "valor"}
#Las claves deben ser unicas.

datos = {"Nombre1": "Yulieth", "Nombre2": "Valentina", "Apellido": "Varela", "Edad": 18}

"""datos1 = dict(Nombre1 = "Yulieth"
              Nombre2 = "Valentina"
              Apellido = "Varela"
              Edad = 18)
print(datos1)"""

#Acceder a un valor del diccionario: get
print(datos["Edad"])
print(datos.get("Apellido"))

#Modificra un valor:
datos["Edad"] = 20
print(datos)

datos["Fecha_Ncto"] = "7/10/1999"
print(datos)

#Eliminar elemntos del diccionario: del, pop()
#del datos["Nombre1"]
datos.pop("Edad")
print(datos)

#Eliminar el ultimo elemento: popitem()
datos.popitem
print(datos)

#Acceder a las claves: Keys()
Clave = datos.keys()
print(Clave)

for Clave in datos.keys():
    print (Clave)

#Acceder a los valores: values()
Valores = datos.values()
print(Valores)

for Valor in datos.keys():
    print (Valor)
    
#Acceder a las claves y los valores: items()
Elementos = datos.items()
print(Elementos)

for element in datos.items():
    print (element)
    
for C, V in datos.items():
    print(C, ":", V)
    
#Update(): Actualizar el diccionario
datos2 = {"Edad": 23, "Fecha_Ncto": "7/10/1999"}
datos.update(datos2)

#Eliminar todos los datos del diccionario: clear()
datos.clear()
print(datos)

#Ejemplo Ejercicio:

#Crear 1 diccionario vacio llamado tienda, el usuario debe ingresar la cantidad de articulos que desee almacenar en la tienda, elementos(Clave), precios(Valor). Si el elemento ya se encuentra en la tienda debe informarlo al usuariol de lo contrario debe ingresarlo. mostrar la información almacenada en tienda (Elemento y Precio).

Tienda = {}
CantidadElementos = int(input("Ingrese la cantidad de elementos de la tienda: "))
for i in range(CantidadElementos):
    Articulo = input("Ingrese el nombre del articulo: ")
    if Articulo in Tienda:
        print(f"El articulo {Articulo} ya se encuentra en la tienda")
    else:
        Precio = int(input(f"Ingrese el precio del {Articulo}"))
        Tienda[Articulo] = Precio
print("********** TIENDA **********")
for Articulo, Precio in Tienda.items():
    print("%s Tiene un precio de: %d" %(Articulo, Precio))