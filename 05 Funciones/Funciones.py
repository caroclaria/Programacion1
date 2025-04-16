# 1 
# Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.
def imprimir_hola():
    print("Hola Mundo!")

imprimir_hola()    

# 2
# Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

saludar_usuario(input("ingrese su nombre"))


# 3
# Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
# dir los datos al usuario y llamar a esta función con los valores ingresados

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

informacion_personal(input("ingrese su nombre"), input("ingrese su apellido"), input("ingrese su edad"), input("ingrese su lugar de residencia"))


# 4
# Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
# dio como parámetro y devuelva el área del círculo. calcular_peri
# metro_circulo(radio) que reciba el radio como parámetro y devuel
# va el perímetro del círculo. Solicitar el radio al usuario y llamar 
# ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    area = 3.14* (radio * radio)
    return area
def perimetro_circulo(radio):
    perimetro = 4.14 * 2 *radio
    return perimetro
def devolver_final (radio):
    
    calcular_area_circulo(radio)
    perimetro_circulo(radio)
    print(f"el area del circulo ingresado es {calcular_area_circulo(radio)}, su perimetro es {perimetro_circulo(radio)}")

devolver_final(int(input("ingrese el radio de un circulo")))

# 5
# Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mos
# trar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos / 3600
    print(f"{segundos} segundos son {horas} horas")
    return horas

segundos_a_horas(int(input("ingrese una cantidad de segundos")))

# 6
# Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la fun
# ción.

def tabla_multiplicar(numero):
    for i in range (1,11):
        resultado = numero * i
        print(f"{numero} * {i} = {resultado}")
tabla_multiplicar(int(input("ingrese un numero")))

# 7
# Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resulta
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
# sultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    print(f"{a} + {b} = {suma}")
    print(f"{a} - {b} = {resta}")
    print(f"{a} * {b} = {multiplicacion}")
    print(f"{a} / {b} = {division}")
operaciones_basicas(int(input("ingrese un numero")), int(input("ingrese otro numero")))
    
# 8
# Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
# ción para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = (peso /altura)/altura
    print(f"su imc es {imc}")

calcular_imc(float(input("ingrese su peso en kg")), float(input("ingrese su altura en metros")))

# 9
# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_farenheit(celsius):
    farenheit = (celsius * 9/5) + 32 
    print(f"{celsius}grados celcius son {farenheit} farenheit")

celsius_a_farenheit(float(input("ingrese una temperatura en grados celsius")))

# 10
# Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función

def calcular_promedio(a, b, c):
    promedio = (a + b +c) /3
    print(f"el promedio de {a}, {b}, {c} es {promedio}")

calcular_promedio(float(input("ingrese un numero")), float(input("ingrese otro numero")),float(input("ingrese otro numero")))