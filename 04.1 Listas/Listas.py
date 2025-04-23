# 1
# Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
# range.
numeros =list(range(4,101,4))

# 2
# Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!
lista_compras = ["arroz" , "aceite", "azucar", "fideos", "carne"]
print(lista_compras[-2])

# 3
# Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
# ejemplo:
palabras = []
palabras.append("gato")
palabras.append("peligro")
palabras.append("mate")
print(palabras)

# 4
# Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)


# 5
# Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
#elimina el numero mayor

# 6
# Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.
numeros2 = list(range(10,31,5))
print(numeros2[0:2])

# 7
# Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "bmw"
autos[2] = "fiat"
print(autos)

# 8
# Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.
dobles = []
dobles.append(10)
dobles.append(20)
dobles.append(30)
print(dobles)

# 9
# Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
# # a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1]="tallarines"
# c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")
# d) Imprimir la lista resultante por pantalla
print(compras)

# 10
# Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)


