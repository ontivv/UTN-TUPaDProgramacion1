#EJERCICIO 1

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*factorial(num-1)

num = int(input("Ingrese un número al que sacar el factorial: "))

print(f"{num}! = {factorial(num)}")

#------------------------------------------------------------------------------
#EJERCICIO 2

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def secuencia_fibo(n):
    a = 0
    b = 1
    
    for i in range(n+1):
        if i == 0:
            print("POSICIÓN 0:0")
        elif i == 1:
            print("POSICIÓN 1:1")
        else:
            c = a+b
            print(f"POSICIÓN {i}: {a} + {b} = {c}")
            
            a=b
            b=c

num = int(input("Ingrese la posición para realizar la secuencia Fibonacci: "))
valor_final = fibonacci(num)
print()
secuencia_fibo(num)

print()
print(f"El valor Fibonacci de la posición {num} es {valor_final}")

#------------------------------------------------------------------------------
#EJERCICIO 3

def calcular_potencia(n,m):
    if m == 0:
        return 1
    else:
        return n*calcular_potencia(n,m-1)

num_base = int(input("Ingresa un número base: "))
num_exp = int(input("Ingresa un número exponente: "))
print()
print(f"El resultado de 5 elevado a la 3 es: {calcular_potencia(num_base,num_exp)}")

#------------------------------------------------------------------------------
#EJERCICIO 4

def convertir_binario(num):
    if num == 0:
        return ""
    else:
        cociente = num//2
        resto = num%2
        return convertir_binario(cociente) + str(resto)

binario_invertido = []
lista_binaria = []

num = int(input("Ingrese un número: "))

while num < 0:
    num = int(input("Número inválido, debe ser entero: "))

if num == 0:
    print("El binario de 0 es 0.")

num_binario = convertir_binario(num)
print()
print(f"El número {num} convertido a binario es: {num_binario}")

#------------------------------------------------------------------------------
#EJERCICIO 5

def palabra_invertida(palabra_normal,letra_p,cont,palabra_invert):
    if cont < 0:
        palabra_final ="".join(palabra_invert).strip().lower()
        if palabra_final == palabra_normal.lower():
            return True
        else:
            return False
    else:
        palabra_invert.append(letra_p[cont])
        return palabra_invertida(palabra_normal,letra_p,cont-1,palabra_invert)


palabra = input("Ingresa una palabra: ")
letras = list(palabra)
pal = []
palabra_invert = []
cont= len(letras)-1
resultado = (palabra_invertida(palabra,letras,cont,palabra_invert))

if resultado:
    print(f"La palabra {palabra} es un palindromo! ({resultado})")
else:
    print(f"La palabra {palabra} no es un palindromo ({resultado})")

#------------------------------------------------------------------------------
#EJERCICIO 6