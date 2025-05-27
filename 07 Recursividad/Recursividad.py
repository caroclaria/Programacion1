# 1
# Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
# función para calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario 

def factorial(num):
    if num==0:
        return 1
    else:
        return num * factorial(num-1)
    
def factorial_del_1_al_n():
    num = int(input("Ingrese un numero entero"))

    for i in range (1, num+1):
        print(f"el factorial de {i} es ",factorial(i))
factorial_del_1_al_n()

# 2
# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
# especifique. 
def pos_fibo(pos):
    if pos == 0:
        return 0
    elif pos==1:
        return 1
    else:
        return pos_fibo(pos -1) + pos_fibo(pos -2)
    
def mostrar_fibonacci():
    num = int(input("idique hasta que posicion de fibonacci quiere que se muestre"))
    for i in range (1,num+1):
        print(f"la posicion {i} en fibonacci representa el numero ",pos_fibo(i))
mostrar_fibonacci()


# 3
# Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
# algoritmo general. 
def recursiva(base, exponente):
    if exponente == 0: #cualquier numero elevado a 0 da 1
        return 1
    elif exponente ==1: #cualquier numero elevado a 1 da el mismo numero
        return base
    else:
        return base * recursiva(base, exponente -1)


print(recursiva(3,3))

# 4
# Crear una función recursiva en Python que reciba un número entero positivo en base 
# decimal y devuelva su representación en binario como una cadena de texto. 

def convertir_a_binario(numero):
    if numero == 0:
        return 0
    elif numero ==1:
        return 1
    else:
        residuo = numero % 2
        cociente = numero//2
        return   str(convertir_a_binario(cociente)) + str(residuo)
    
print(convertir_a_binario(50))

# 5
# Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
# lo es. 
#      Requisitos: 
# La solución debe ser recursiva. 
# No se debe usar [::-1] ni la función reversed(). 
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])    
    else:
        return False
    
print(es_palindromo("neuquen"))

# 6
# Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
# número entero positivo y devuelva la suma de todos sus dígitos. 
#      Restricciones: 
# No se puede convertir el número a string. 
# Usá operaciones matemáticas (%, //) y recursión. 
def suma_digitos(numero):
    if numero == 0:
        return 0
    elif numero //10 == 0:
        return numero
    else:
        return numero %10 + (suma_digitos(numero//10))
print(suma_digitos(1234))

# 7
# Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
# último nivel con un solo bloque. 
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
# pirámide. 
#       Ejemplos: 
# contar_bloques(1)   → 1         (1) 
# contar_bloques(2)   → 3         (2 + 1) 
# contar_bloques(4)   → 10        (4 + 3 + 2 + 1) 
def contar_bloques(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return numero + contar_bloques(numero -1)

print(contar_bloques(5))

# 8
# Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
# aparece ese dígito dentro del número.
suma=0
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero %10 == digito:
        return 1 + (contar_digito(numero//10, digito))
    else:
        return contar_digito(numero//10, digito)
    
print(contar_digito(3554353555,5))