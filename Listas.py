#Las listas se representan con []
lista = [] #lista vacía
listas = [1, 1.30, "Hola", True, False] #Enteros, Decimales, String, booleano, cada dato debe ser separado con (,)

#Mutables: modificar
#Indexadas
#Metodo len(): Muestra la Longitud de la lista
print(len(listas)) #Muestra la cantidad de elementos que tiene la lista

#Acceder a la lista
print(listas[2]) #Se escribe el nombre de la lista y entre [] la posición del objeto que quiere ver
print(listas[2]) #Si se quiere acceder de forma inversa

#Modificar elemento
listas[2]="Colecciones"
print (listas)

#Recorrer una lista
for elemento in listas:
    print(elemento)

#Indice (posición)
for elem in range (len(listas)):
    print(f"{listas[elem]} Estan en la posición {elem}") #Recorre rango desde 0

#Insertar elementos: insert(posicion, dato o elemento a ingresar),append(dato o elemento a ingresar) ingresa el elemento en la ultima posicion
Marcas_Autos = ["Renault", "Chevrolet", "Suzuki", "Audi", "Kia"]
Marcas_Autos.insert(3, "Mazda") #Acá primero se pone la posición en la que quiere el nuevo elemento seguido del nombre que quiere agregar
Marcas_Autos.append("Toyota") #El append es para que el elemento agregado quede de ultima posición
print(Marcas_Autos)

#eliminar elementos
#pop(indica la posicion del elemento que va a eliminar), remove(indica el elemento a eliminar)
Marcas_Autos.pop(4)
print(Marcas_Autos)

#Conocer la posicion del elemento:index(elemento)
posicion = Marcas_Autos.index("suzuki")
print(posicion)

#ORGANIZAR LISTA: ascendente sort(),descendente sort(reverse=true)

Marcas_Autos.sort()
print(Marcas_Autos)
Marcas_Autos.sort(reverse=True)
print(Marcas_Autos)

#EXTENDER LA LISTA :extend(lista)
otras_marcas = ["BMW","Ferrari","Tesla","Mercesdes bena"]
Marcas_Autos.extend(otras_marcas)
print(Marcas_Autos) 

#Recorrer 2 o mas listas al mismo tiempo 
Animales = ["Gato","Leon","Ballena","Pajaro","Serpiente"]
Tipo_A = ["Terrestre","Salvaje","Mamifero","Aereo","Reptil"]

for Animal,tipo in zip (Animales,Tipo_A):
    print(f"aca los animal {Animal} y el tipos {tipo}")
    
#Contar elementos repetidos count(elemento)
numeros = [1,2,3,4,5,1,345,1,45,2,1,1,1,456]
Contar = numeros.count(1)
print(Contar)

