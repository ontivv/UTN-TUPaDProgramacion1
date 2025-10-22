#EJERCICIO 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450,}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#---------------------------------------------------------
#EJERCICIO 2

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

#---------------------------------------------------------
#EJERCICIO 3

nombre_frutas = precios_frutas.keys()
print(nombre_frutas)

#---------------------------------------------------------
#EJERCICIO 4

numeros_telefonicos = {"Mariela": "2615952315","Juan": "2618079283","Roberto": "2613459607",
                        "Marcelo": "2615436722","Carlos": "2614050092"}

reintentar = "S"

while reintentar == "s" or reintentar == "S":
    
    consulta = input("Nombre del contacto a buscar (CON MAYÚSCULA INICIAL): ")

    if consulta in numeros_telefonicos:
        print(f"Contacto: {consulta} ({numeros_telefonicos[consulta]})")
        print("¿desea intentar nuevamente?")
        reintentar = input("S/N : ")
    else:
        print("Contacto no encontrado, ¿desea intentar nuevamente?")
        reintentar = input("S/N : ")

#----------------------------------------------------------
#EJERCICIO 5

frase = input("Ingrese una frase: ")
palabras = frase.split(" ")

palabras_unicas = set()

for i in range(len(palabras)):
    palabras_unicas.add(palabras[i])

contador = {}

for palabra in palabras:
    contador[palabra] = palabras.count(palabra)

print(f"PALABRAS UNICAS: {palabras_unicas}")
print()
print(f"CONTADOR: {contador}")

#----------------------------------------------------------
#EJERCICIO 6

alumnos_notas = {}
alumnos = ["" for _ in range(3)]
notas = [0 for _ in range(3)]
contador = 0

for i in range(3):
    alumnos[i] = input("Nombre de alumno: ")

for alumno in alumnos:
    
    print()
    print(f"Notas {alumno}")
    nota = [0 for _ in range(3 )]
    
    for i in range(3):
        
        nota[i] = float(input(f"Nota {i+1}: "))
        notas[i] = nota[i] 
        
        alumnos_notas[alumno] = tuple(notas)

print()
print("ALUMNOS Y NOTAS:")

for alumno in alumnos:
    print()
    print(f"""NOTAS {alumno}: 
            {alumnos_notas[alumno]}""")


#----------------------------------------------------------
#EJERCICIO 7

parcial1_aprobados = {1,2,3,4,5,6,7,8,9}
parcial2_aprobados = {1,2,6,7,8}

ambos_parciales_aprobados = parcial1_aprobados.intersection(parcial2_aprobados)
un_parcial_aprobado = parcial1_aprobados.difference(parcial2_aprobados)
almenos_uno_aprobado = parcial1_aprobados.union(parcial2_aprobados)

print(f"ALUMNOS QUE APROBARON AMBOS PARCIALES: {ambos_parciales_aprobados}")
print()
print(f"ALUMNOS QUE APROBARON UN SOLO PARCIAL: {un_parcial_aprobado}")
print()
print(f"ALUMNOS QUE APROBARON ALMENOS UNO: {almenos_uno_aprobado}")

#----------------------------------------------------------
#EJERCICIO 8

productos = {"Leche": 30 , "Fideos": 0 , "Papas" : 10 , "Prepizzas": 15}
productos_nombre = ["Leche","Fideos","Papas","Prepizzas"]

continuar_main = 1

def repetir_proceso(seguir):
    
    seguir = (input("""¿Desea realizar el proceso nuevamente?
                                        
                                            (SI) S/N (NO)
                                        
                                        """))
    
    while seguir != "S" and seguir != "s" and seguir != "N" and seguir != "n":
                
                    seguir = (input("""
                                        
                                        Valor inválido, intente nuevamente:
                                                (SI) S/N (NO)
                                        
                                        """))
    
    return seguir


while continuar_main == 1:

    continuar = "S"

    menu = int(input("""¿QUÉ OPERACIÓN DESEA REALIZAR?
                        
                        (1) Consultar stock de producto
                        (2) Agregar unidades a producto existente
                        (3) Agregar un nuevo producto
                        (4) Salir del programa
                        
                        """))

    match menu:
        
        case 1:  
            
            while continuar == "S" or continuar == "s":
                
                consulta = (input("¿Qué producto desea buscar? ")).capitalize()

                if consulta in productos_nombre: 
                    
                    if productos[consulta] == 0:
                        print()
                        print(f"{consulta} - (PRODUCTO SIN STOCK)")
                    
                    else:
                        print()
                        print(f"{consulta} - {productos[consulta]} Unidades Disponibles.")
                
                else: 
                    print("PRODUCTO NO REGISTRADO.")
                
                continuar = repetir_proceso(continuar)
        
        case 2:
            
            while continuar == "S" or continuar == "s":
                
                consulta = (input("¿Qué producto desea buscar? ")).capitalize()

                if consulta in productos_nombre: 
                    
                    adicion_unidades = int(input("¿Cuantas unidades desea añadir? "))
                    
                    if adicion_unidades == 0:
                            print("No hay nada que añadir")
                            pass
                    
                    while adicion_unidades < 0:
                        adicion_unidades = int(input("Valor inválido, intente nuevamente: "))
                    
                    productos[consulta] += adicion_unidades
                    
                    print()
                    if adicion_unidades == 0:
                        print("STOCK SIN MODIFICACIONES:")
                        print(f"{consulta} - {productos[consulta]} Unidades disponibles")
                    else:
                        print("STOCK ACTUALIZADO:")
                        print(f"{consulta} - {productos[consulta]} Unidades disponibles")
                
                else:
                    
                    print()
                    print("PRODUCTO NO ENCONTRADO.")
                
                continuar = repetir_proceso(continuar)
        
        case 3:
            
            while continuar == "S" or continuar == "s":
                nuevo_producto = input("NOMBRE DEL NUEVO PRODUCTO: ").capitalize()
                productos[nuevo_producto] = int(input("CANTIDAD DE UNIDADES: "))
                
                while productos[nuevo_producto] < 0:
                    
                    productos[nuevo_producto] = int(input("VALOR INVÁLIDO, INTENTE NUEVAMENTE: "))
            
                continuar = repetir_proceso(continuar)
        case 4:
            print("FIN DEL PROGRAMA")
            continuar_main = 0

#----------------------------------------------------------
#EJERCICIO 9

pregunta = "S"
pregunta2 = ""
agenda = {}

def asignacion_consulta(c):
    consulta_dia = input("Ingrese día (dd/mm): ")
    consulta_hora = input("Ingrese hora (hs:m): ")
    
    c = (consulta_dia,consulta_hora)
    return c

def titulo(j):
        
    if j == 0:
        print("PRIMER ASUNTO:")
        
    elif j == 2:
        print("SEGUNDO ASUNTO:")

def repetir_proceso(seguir):        
    seguir = (input("¿Desea realizar el proceso nuevamente? (S/N): ")).upper()
        
    while seguir != "S" and seguir != "N":
                    
        seguir = (input("Valor inválido, intente nuevamente (S/N: ")).upper()
        
    return seguir

def consulta(cons):
    cons = (input("¿Desea consultar alguna reunion? (S/N): ")).upper()
    
    while cons != "S" and cons != "N":
                    
        cons = (input("Valor inválido, intente nuevamente (S/N): ")).upper()
        
    return cons


while pregunta == "S":
    print()
    print("CREACIÓN DE AGENDA:")

    for i in range(2):
        
        dia = input("Ingrese día: ")
        hora = input("Ingrese horario: ")
        asunto = input("Ingrese asunto: ")
        agenda[dia,hora] = asunto
    
    
    pregunta = repetir_proceso(pregunta)
    pregunta2 = consulta(pregunta2)

    while pregunta2 == "S":
        
        consulta = asignacion_consulta(consulta)
        
        agenda_keys = agenda.keys()
        
        if consulta in agenda_keys:
            
            print(f"{consulta} - {agenda[consulta]}")
        
        else:
            print("Asunto no registrado.")
        pregunta2 = repetir_proceso(pregunta2)
        if pregunta2 == "N":
            pregunta == "N"

#----------------------------------------------------------
#EJERCICIO 10

original = {"Argentina" : "Buenos Aires" , "EEUU" : "Washington DC" , "España" : "Madrid"}
original_keys = original.keys()
invertido = {}

for keys in original_keys:
    invertido[original[keys]] = keys
    
print(f"""Original: {original}
        
Invertido: {invertido}
        
        """)