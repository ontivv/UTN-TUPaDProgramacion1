continuar = 1

tarjetas = ["1234567890123456", "9876543210987654", "5555666677778888"]
saldos = [150.50, 25.00, -10.00]

while continuar == 1:
    
    print()
    
    opcion = int(input("""¿Qué operación desea realizar?
                        
                        (1) Crear nueva lista de tarjetas
                        (2) Mostrar todas las tarjetas registradas
                        (3) Consultar saldo por número
                        (4) Listar saldos en negativo o cero
                        (5) Agregar tarjeta
                        (6) Cargar/Debitar saldo
                        (7) Salir
                        
                        """))
    
    
    match opcion:
        
        case 1:
            
            print()
            cant_tarjetas = int(input("¿Cuantas tarjetas desea agregar?: "))
            
            while cant_tarjetas < 0:
                print()
                cant_tarjetas = int(input("Cantidad inválida, ingrese nuevamente: "))
            
            if cant_tarjetas == 0:
                
                print()
                print("No hay tarjetas para agregar")
                continue
            
            tarjetas = ["" for _ in range(cant_tarjetas)]
            saldos = [0 for _ in range(cant_tarjetas)]
            
            for i in range(cant_tarjetas):
                
                print()
                tarjetas[i] = input("Número de tarjeta: ")
                saldos[i] = int(input("Saldos de la tarjeta: "))
            
            print()
            print()
            continuar = int(input("""¿Desea realizar otra operacion?
                                    
                                    (1) SI
                                    (0) NO
                                    
                                    """))
            
        
        
        case 2:
            
            cant_tarjetas = len(tarjetas)
            
            print()
            print("TARJETAS REGISTRADAS:")
            
            for i in range(cant_tarjetas):
                
                print(f"{tarjetas[i]} - saldo: {saldos[i]}")
            
            
            print()
            print()
            continuar = int(input("""¿Desea realizar otra operacion?
                                    
                                    (1) SI
                                    (0) NO
                                    
                                    """))
        
        case 3:
            
            cant_tarjetas = len(tarjetas)

            for i in range(cant_tarjetas):
                
                tarjetas[i] = tarjetas[i]
            
            
            tarjeta_buscada = input("Tarjeta buscada: ")
            
            if tarjeta_buscada in tarjetas:
                
                print("TARJETA REGISTRADA :")
                print()
                
                pos_tarjeta = tarjetas.index(tarjeta_buscada)
                
                print(f"{tarjetas[pos_tarjeta]} - saldo: {saldos[pos_tarjeta]}")
                
            else:
                
                print("La tarjeta buscada no se encuentra registrada.")
            
            print()
            print()
            continuar = int(input("""¿Desea realizar otra operacion?
                                    
                                    (1) SI
                                    (0) NO
                                    
                                    """))
        
        case 4:
            
            cant_tarjetas = len(tarjetas)
            contador = 0
            
            for i in range(cant_tarjetas):
                
                if saldos[i] <= 0:
                    
                    contador += 1
            
            if contador > 0:
                
                print("TARJETAS EN NEGATIVO O CERO:")
                print()
                
                for i in range(cant_tarjetas):
                
                    if saldos[i] <= 0:
                    
                        print(f"{tarjetas[i]} - saldo: {saldos[i]}")
            
            else:
                print("No hay tarjetas con saldo negativo.")
            
            print()
            print()
            continuar = int(input("""¿Desea realizar otra operacion?
                                    
                                    (1) SI
                                    (0) NO
                                    
                                    """))
        
        case 5:
            
            cant_tarjetas = int(input("¿Cuantas tarjetas desea agregar?: "))
            
            for i in range(cant_tarjetas):
                
                tarjetas.append(input("Número de la tarjeta: "))
                saldos.append(float(input("Saldo: ")))
            
            print()
            print()
            continuar = int(input("""¿Desea realizar otra operacion?
                                    
                                    (1) SI
                                    (0) NO
                                    
                                    """))
        
        case 6:
            
            cant_tarjetas = len(tarjetas)

            for i in range(cant_tarjetas):
                
                tarjetas[i] = tarjetas[i]
            
            
            tarjeta_buscada = input("Tarjeta buscada: ")
            
            if tarjeta_buscada in tarjetas:
                
                print("TARJETA REGISTRADA")
                print()
                
                pos_tarjeta = tarjetas.index(tarjeta_buscada)
                
                decision = int(input("""¿Qué operación desea realizar?
                                        
                                        (1) CARGA
                                        (2) DÉBITO
                                        
                                        """))
                
                print()
                
                match decision:
                    
                    case 1:
                        
                        cant_carga = float(input("¿Cuanto desea agregar?: "))
                        
                        while cant_carga <= 0:
                            print()
                            cant_carga = int(input("Cantidad inválida, ingrese nuevamente: "))
                        
                        saldos[pos_tarjeta] += cant_carga
                        
                        print()
                        print("CANTIDAD CARGADA CORRECTAMENTE: ")
                        print(f"{tarjetas[pos_tarjeta]} - saldo: {saldos[pos_tarjeta]}")
                        
                    
                    
                    case 2:
                        
                        cant_debito = float(input("¿Cuanto desea debitar?: "))
                        
                        while cant_debito <= 0:
                            print()
                            cant_debito = int(input("Cantidad inválida, ingrese nuevamente: "))
                        
                        saldos[pos_tarjeta] -= cant_debito
                        
                        print()
                        print("CANTIDAD DEBITADA CORRECTAMENTE: ")
                        print(f"{tarjetas[pos_tarjeta]} - saldo: {saldos[pos_tarjeta]}")
                
                
                
                
                
            else:
                
                print("La tarjeta buscada no se encuentra registrada.")
            
            
            
            print()
            print()
            continuar = int(input("""¿Desea realizar otra operacion?
                                    
                                    (1) SI
                                    (0) NO
                                    
                                    """))
        
        case 7:
            
            print()
            print("FIN DEL PROGRAMA")
            continuar = 0