continuar = 1

ejem_positivo = 0

titulos = ["Harry Potter y la Piedra Filosofal","El Resplandor","Viaje al Centro de la Tierra"]
ejemplares = [11,0,5]

repeticion_menu = 1


op = int(input("""¿Qué operación desea realizar?
            
                (1) Agregar libros al catálogo
                (2) Consultar catálogo
                (3) Mostrar catálogo completo
                (4) Devoluciones
                
                
                """))

if op == 1 :

    while continuar == 1 :
        cant_titulos = int(input("¿Cuántos libros desea agregar al catalogo? : "))

        print("")
        print("")

        for i in range(cant_titulos) :
    
            titulos[i] = input("Ingrese el nombre del libro: ")
    
            ejemplares[i] = int(input("Ingrese los ejemplares del libro disponibles: "))


        print("")
        print("")
        print("DEMOSTRACIÓN DE CATÁLOGO DE LIBROS: ")

        for i in range(len(titulos)) :
    
            print(f" LIBRO: {titulos[i]}  -  EJEMPLARES: {ejemplares[i]} ")

    
        print("")
        print("")
    
    
        continuar = int(input("""¿Desea añadir más libros?
    
                        (1) SI
                        (0) NO
    
                            """))
    
        print("")
        print("")
    
        mas_libros = 0
    
        if continuar == 1 :
        
            mas_libros = 1
        
        while mas_libros == 1 :
        
            cant_libros = int(input("¿Cuántos libros desea añadir?: "))
        
            print("")
            print("")
        
            for i in range(cant_libros):
    
                nombre_libro = input("Título del libro a agregar: ")
                titulos.append(nombre_libro)
            
                cant_libro_adherido = int(input("Cantidad de ejemplares del libro: "))
                ejemplares.append(cant_libro_adherido)
        
            mas_libros = int(input("""¿Desea añadir más libros?
    
                                    (1) SI
                                    (0) NO
    
                            """))
            if mas_libros == 0 :
        
                continuar = 0




if op == 2 :

    consulta = int(input("""¿Desea consultar el catálogo?
                
            (1) SI
            (0) NO
            
            """))
    
    print("")
    
    while consulta == 1 :
        
        for i in range(len(titulos)) :
        
            titulos[i] = titulos[i].lower()
    
        nombre = input("Ingrese el nombre del libro: ")
        
        nombre = nombre.lower()
    
    
        print("")
        print("")
    
    
        if nombre in titulos :
        
                posicion = titulos.index(nombre)
    
                print(f"""Libro en el catálogo!
        
                        {titulos[posicion].title()}  -  {ejemplares[posicion]} ejemplares disponibles.
        
                        """)
        else :
            
            print("Libro no disponible.")
    
        consulta = int(input("""¿Desea consultar de nuevo?
    
                    (1) SI
                    (0) NO
    
                        """))


if op == 3 :
    
    catalogo_compl = int(input("""¿Desea ver el catalogo completo?
                            
                                (1) SI
                                (0) NO
                            
                            """))

    cant_de_titulos = len(titulos)

    sin_stock = ["" for _ in range(cant_de_titulos)]
    con_stock = ["" for _ in range(cant_de_titulos)]

    sin_stock_num = [0 for _ in range(cant_de_titulos)]
    con_stock_num = [0 for _ in range(cant_de_titulos)]

    while catalogo_compl == 1 :
    
        for i in range(cant_de_titulos) :
        
            if ejemplares[i] == 0 :
            
                sin_stock[i] = titulos[i]
                sin_stock_num[i] = ejemplares[i]
            
            else :
            
                con_stock[i] = titulos[i]
                con_stock_num[i] = ejemplares[i]



        print("")
        print("")

        print("TÍTULOS CON STOCK:")
        print("")
    
        for i in range(len(con_stock)) :
    
            print(con_stock[i].title()) 

        print("")

        repeticiones = sin_stock.count("")

        if repeticiones == len(titulos) :
            pass

        else:
    
            print("TÍTULOS SIN STOCK:")
    
            for i in range(len(sin_stock)) :
        
                print(sin_stock[i].title())

                print("")
                print("")
    
    
        catalogo_compl = 0


if op == 4 :
    prestamo = int(input("""¿Desea realizar la devolución de algún libro del catálogo?
                        
                        (1) SI
                        (0) NO
                        
                        """))

    while prestamo == 1 :
        
        libro = input("¿Qué libro desea devolver? : ")
        
        libro = libro.lower()
        
        cant_de_titulos = len(titulos)
        
        for i in range(cant_de_titulos) :
            titulos[i] = titulos[i].lower()
        
        if not(libro in titulos) :
            
            esta_en_catalogo = False
            intentos = 0
            
            while esta_en_catalogo == False :
                print("El libro que desea devolver no se encuentra en el catálogo.")
                libro = input("Intente nuevamente: ")
                
                intentos += 1
                
                if libro in titulos :
                    
                    esta_en_catalogo = True
                
                if intentos == 3 :
                    
                    conclusion = int(input("""¿Realmente su libro se encuentra en el catálogo?
                                            
                                            (1) SI
                                            (0) NO
                                            
                                            """))
                
                    if conclusion == 0 :
                        
                        prestamo = 0    
                        break
                    
        
        
        elif libro in titulos :
            
            posicion_libro = titulos.index(libro)
            
            ejemplares[posicion_libro] += 1

            
            print("")
            print("¡El libro se encuentra en el catálogo! Muchas gracias por su devolución de libro prestado.")
            print("")
            print("CATÁLOGO ACTUALIZADO: ")
            print("")
            
            for i in range(cant_de_titulos) :
                
                print(f"{titulos[i].title()} - {ejemplares[i]} ejemplares disponibles")
                print("")
            
            prestamo = 0