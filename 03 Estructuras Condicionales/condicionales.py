#1
#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
print("ejercicio 1")
edad = int(input("ingrese su edad"))
if edad > 18:
    print("Es mayor de edad")

#2
# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”
print("ejercicio 2")
nota = int(input("ingrese su nota"))
if nota >= 6:
    print("Aprobado")
else: 
    print("Desaprobado")

#3
# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.
print("ejercicio 3")
num = int(input("inrese un numero"))
if num %2==0:
    print("ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

# 4
#  Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.
print("ejercicio 4")
edad = int(input("ingrese su edad"))
if edad <12:
    print("niño")
elif edad >= 12 and edad <18:
    print("adolescente")
elif edad >= 18 and edad<30:
    print("Adulto joven")
elif edad>= 30:
    print("adulto")

# 5
# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.
print("ejercicio 5")
password = str(input("ingrese una contraseña"))
if len(password) >= 8 and len(password) <= 14:
    print("ha ingresado una contraseña correcta")
else:
    print("Ingrese una contraseña entre 8 y 14 caracteres")

# 6
# escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla
print("ejercicio 6")
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if media > mediana and mediana > moda:
    print("sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("sesgo negativo o a la izquierda")
elif media == mediana and media == moda:
    print("sin sesgo")

# 7
# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.
print("ejercicio 7")
frase = str(input("ingrese una frase"))
if frase[len(frase)-1] == "a" or frase[len(frase)-1] == "e" or frase[len(frase)-1] == "i" or frase[len(frase)-1] == "0" or frase[len(frase)-1] == "u":
    frase_final = frase + "!"
    print(frase_final)
else:
    print(frase)

# 8 
# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.
print("ejercicio 8")
nombre = str(input("ingrese su nombre"))
elegido = int(input("presione 1 si quiere su nombre en mayusula, 2 en minuscula, 3 con primera letra en mayuscula"))
if elegido ==1 :
    print(nombre.upper())
elif elegido == 2:
    print(nombre.lower())
elif elegido == 3:
    print(nombre.title())

# 9
# Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)
print("ejercicio 9")
magnitud = float(input("ingrese la magnitud del terremoto"))
if magnitud <3:
    print("muy leve")
elif magnitud >=3 and magnitud <4:
    print("leve")
elif magnitud >= 4 and magnitud <5:
    print("moderado")
elif magnitud>=5 and magnitud <6:
    print("fuerte")
elif magnitud>=6 and magnitud<7:
    print("muy fuerte")
elif magnitud >=7:
    print("extremo")

# 10
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano
print("ejercicio 10")
hemisferio = str(input("ingrese N si es hemisferio norte o s s es hemisferio sur"))
dia = int(input("ingrese que dia del año es"))
mes = int(input("ingrese el mes en numero"))
estacion = ""
if hemisferio.lower() == "n":
    if (mes== 1 or mes == 2) or (mes == 12 and dia >=21) or (mes == 3 and dia <=20):
        estacion = "invierno"
    elif (mes == 4 or mes == 5) or (mes == 3 and dia >= 21) or (mes == 6 and dia <=20):
        estacion = "primavera"
    elif (mes == 7 or mes == 8) or (mes == 6 and dia >= 21) or (mes == 9 and dia <=20):
        estacion="verano"
    elif (mes == 10 or mes == 11) or (mes == 9 and dia >= 21) or (mes == 12 and dia <=20):
        estacion= "otoño"

elif hemisferio.lower() == "s":
    if (mes== 1 or mes == 2) or (mes == 12 and dia >=21) or (mes == 3 and dia <=20):
        estacion = "verano"
    elif (mes == 4 or mes == 5) or (mes == 3 and dia >= 21) or (mes == 6 and dia <=20):
        estacion = "otoño"
    elif (mes == 7 or mes == 8) or (mes == 6 and dia >= 21) or (mes == 9 and dia <=20):
        estacion="invierno"
    elif (mes == 10 or mes == 11) or (mes == 9 and dia >= 21) or (mes == 12 and dia <=20):
        estacion= "primavera"
print(f"usted esta en la estacion {estacion}")
    