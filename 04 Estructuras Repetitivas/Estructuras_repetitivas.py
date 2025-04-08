# 1
# Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)

# 2
# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

num2 = int(input("ingrese un numero entero"))
digito = 0
while num2 !=0:
    num2 = (int(num2/10))
    digito +=1
print(f"el numero ingresado {num2} tiene {digito} digitos")


# 3
# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num_inicial = int(input("ingrese un numero"))
num_final = int(input("ingrese otro numero"))
suma= 0
for i in range (num_inicial +1 , num_final):
        suma = suma + i
print(suma)

# 4
# Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

numero = float(input("ingrese un numero diferente a 0"))
acu = 0
while numero !=0:
    acu = acu + numero
    numero = float(input("ingrese otro numero, ingrese 0 si no quiere continuar"))
print(f"la suma de los numeros ingresados es {acu}")


# 5
# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
numero_aleatorio = random.randint(0,9)
num5 = int(input("intenta adivinar un numero del 0 al 9"))
intentos = 1
while num5 != numero_aleatorio:
    num5 = int(input("intenta adivinar un numero del 0 al 9"))
    intentos += 1
print(f"requeriste {intentos} para adivinar el numero")


# 6
# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100,0,-2):
    if i %2 ==0:
        print(i)

# 7
# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num7 = int(input("ingrese un numero entero positivo"))
suma = 0
for i in range(0,num7):
    suma = suma + i
print(suma)

# 8
# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

positivo = 0
negativo = 0
impar = 0
par = 0
for i in range (100):
    num8 = int(input("ingrese un numero entero diferente a 0"))
    if num8 % 2 == 0:
        par +=1
    else:
        impar +=1
    if num8 > 0:
        positivo +=1
    else:
        negativo +=1
print(f"los numeros positivos ingresados fueron:{positivo}, los negativos:{negativo}, pares:{par}, impares:{impar}")
        

# 9
# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

sumatoria= 0
for i in range (100):
    num9 = int(input("ingrese un numero entero"))
    sumatoria = sumatoria + num9
media = sumatoria /100
print(f"la media de los valores ingresados es:{media}")

# 10
# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num10 = int(input("ingrese un numero entero"))
cifra =0
inverso = 0
while num10 !=0:
    cifra = num10 %10
    num10 = int(num10/10)
    inverso = inverso * 10 + cifra
print(inverso)