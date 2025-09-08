#EJERCICIO 1

m1= input("Mensaje 1: ")
m2= input("Mensaje 2: ")
m3= input("Mensaje 3: ")
m4= input("Mensaje 4: ")
m5= input("Mensaje 5: ")

mensajes = [m1,m2,m3,m4,m5]

desplazamiento=2


for i in range(5):

    m_encriptado=""
    
    print("")
    
    msj= mensajes[i]
    
    for letra in msj:
        codigo= ord(letra)

        nuevo_codigo= codigo+desplazamiento

        m_encriptado+= chr(nuevo_codigo)

    print(m_encriptado)
    
    
    
    
#----------------------------------------------------------------------
#EJERCICIO 2


print("")
print("")

repeticion= 1
seleccion_correcta= True

while repeticion==1 and seleccion_correcta:

    jugada_player= int(input("""Ingrese su jugada:
                        Piedra (0)
                        Papel  (1)
                        Tijera (2)
                    """))

    if jugada_player<0 or jugada_player>2:
        
        print("Selección inválida, intente nuevamente.")
        
    else:
        
        if jugada_player==0:
    
            jugada_final_player= "Piedra"
            print("JUGADA: Piedra")
        elif jugada_player==1:
    
            jugada_final_player= "Papel"
            print("JUGADA: Papel")
        else:
            jugada_final_player= "Tijera"
            print("JUGADA: Tijera")
    
    
    
    
        import random

        jugada_cpu= random.randint(0,2)


        if jugada_cpu==0:
    
            jugada_final_cpu= "Piedra"
            print("JUGADA CPU: Piedra")
        
        elif jugada_cpu==1:
    
            jugada_final_cpu= "Papel"
            print("JUGADA CPU: Papel")
        
        else:
            jugada_final_cpu= "Tijera"
            print("JUGADA CPU: Tijera")

        print("")
    
    
    
    
        puntos_player= 0
        puntos_cpu=0
    
    
    
        if jugada_player==jugada_cpu:
            print("")
            print("EMPATE")
        
        
        elif jugada_player==1 and jugada_cpu==0:
            print("")
            print("GANA JUGADOR (PAPEL LE GANA A PIEDRA)")
            puntos_player+=1
        
        elif jugada_player==0 and jugada_cpu==1:
            print("")
            print("GANA CPU (PAPEL LE GANA A PIEDRA)")
            puntos_cpu=0
    
    
    
    
        elif jugada_player==2 and jugada_cpu==1:
            print("")
            print("GANA JUGADOR (TIJERA LE GANA A PAPEL)")
            puntos_player+=1

        elif jugada_player==1 and jugada_cpu==2:
            print("")
            print("GANA CPU (TIJERA LE GANA A PAPEL)")
            puntos_cpu=0
        
        
        
        elif jugada_player==0 and jugada_cpu==2:
            print("")
            print("GANA PLAYER (PIEDRA LE GANA A TIJERA)")
            puntos_player+=1
        
        elif jugada_player==2 and jugada_cpu==0:
        
            print("")
            print("GANA CPU (PIEDRA LE GANA A TIJERA)")
            puntos_cpu=0
    
    
    
    
        repeticion= int(input("""¿Desea jugar nuevamente?    
            
                    (0) NO
                    (1) SI
            """))
    
    
    
    
        while repeticion<0 or repeticion>1:
        
            repeticion=(int(input("Número inválido, ingrese nuevamente: ")))
        
        
print("")

print(f"""  Puntos Obtenidos: {puntos_player}
    Puntos del CPU: {puntos_cpu}
        """)