#Ejercicio
#Crear 2 listas vacias una llamada tienda, otra llamada precio, el usuario debe ingresar el numero de articulos de la tienda y los elementos de cada lista, estos elementos deben ser agregados a la lista correspondiente. debe mostrar los elementos de la tienda con su respectivo precio. (for o while)

# Creamos las listas vacías
tienda = []
precio = []

# Solicitamos al usuario el número de artículos
num_articulos = int(input("Ingrese el número de artículos: "))

# Ciclo para solicitar los elementos de cada lista
for i in range(num_articulos):
    # Solicitamos el nombre del artículo
    nombre_articulo = input("Ingrese el nombre del artículo: ")
    # Solicitamos el precio del artículo y lo convertimos a float
    precio_articulo = float(input("Ingrese el precio del artículo: "))
    # Agregamos los elementos a las listas correspondientes
    tienda.append(nombre_articulo)
    precio.append(precio_articulo)

# Mostramos los elementos de la tienda con su respectivo precio
print("Lista de artículos y precios:")
for i in range(num_articulos):
    print(tienda[i] + ": $" + str(precio[i]))

