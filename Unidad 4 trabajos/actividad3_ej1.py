num_positivo = False

numero = 0

num = int(input("Ingrese un número entero: "))

if num > 0:
    num_positivo = True

while num_positivo == False :
    
    num = int(input("El número ingresado no es entero. Intente nuevamente: "))
    
    if num > 0:
        num_positivo = True

print("")
print("Entre el número ingresado y cero, los números pares son: ")
print("")

for numero in range(num,0,-1) :
    
    if numero % 2 == 0 or numero == 0:
        print(numero, end = " ")