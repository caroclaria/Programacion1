#1
print ("Hola Mundo!")

#2
nombre = input("Ingrese su nombre")
print (f"Hola {nombre}")

#3
nombre = input("ingrese su nombre")
apellido = input("ingrese su apellido")
edad = input("ingrese su edad")
residencia = input("ingrese su lugar de residencia")
print(f"soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4
radio = float(input("ingrese el radio de un circulo"))
perimetro = 2 * 3.14 * radio
area = 3.14 * radio * radio
print(f"el perimetro del circulo es: {perimetro}, el area del circulo es: {area}")

# #5
seg = int(input("ingrese una cantidad de segundos"))
horas = seg / 60
print (f"{seg} segundos equivalen a {horas} horas")

# #6
numero = int(input("ingrese un numero del 1 al 10"))
tabla1 = numero *1
tabla2= numero*2
tabla3 = numero *3
tabla4 = numero *4
tabla5 = numero *5
tabla6 = numero *6
tabla7 = numero * 7
tabla8 = numero *8
tabla9 = numero * 9
tabla10 = numero *10
print(f"{numero} x 1 = {tabla1}")
print(f"{numero} x 2 = {tabla2}")
print(f"{numero} x 3 = {tabla3}")
print(f"{numero} x 4 = {tabla4}")
print(f"{numero} x 5 = {tabla5}")
print(f"{numero} x 6 = {tabla6}")
print(f"{numero} x 7 = {tabla7}")
print(f"{numero} x 8 = {tabla8}")
print(f"{numero} x 9 = {tabla9}")
print(f"{numero} x 10 = {tabla10}")

# #7
num1= int(input("ingrese un numero"))
num2 = int(input("ingrese otro numero"))
suma = num1 + num2
resta = num1- num2
mult = num1 * num2
division = num1 / num2
print(f"la suma de los numeros es {suma}, su resta {resta}, su division {division}, y su multiplicacion {mult}")

# #8
peso = float(input("ingrese su peso"))
talla = float(input("ingrese su talla en m"))
imc = peso /talla /talla
print (f"su indice de masa corporal es: {imc}")

# #9
celcius = float(input("ingrese una temperatura en celcius"))
farenheit = 9/5*celcius +32
print(f"los grados {celcius} representan {farenheit} en grados farenheit")


#10
n1= int(input("ingrese un numero"))
n2=int(input("ingrese un numero"))
n3=int(input("ingrese un numero"))
promedio = (n1 + n2 + n3 )/3
print(f"el promedio de los numeros ingresados es: {promedio}")