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