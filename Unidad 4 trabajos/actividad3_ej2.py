num = int(input("Ingrese un número entre el 1 y el 10: "))

while num<1 or num>10 : 
    num = int(input("Número inválido, ingrese nuevamente: "))

print("")
print("La tabla del número ingresado es: ")

for multi in range(1, 10+1 ,1) :
    
    print(f"{num} x {multi} = {num*multi}")