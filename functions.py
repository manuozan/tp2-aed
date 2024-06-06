
import os

def procesar_timestamp(timestamp):
    if "SC" in timestamp:
        return "Soft Control"
    elif "HC" in timestamp:
        return "Hard Control"
    

def clear_console():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Linux y macOS
    else:
        os.system('clear')


def procesar_direccion(direc, control):
    if control != "Hard Control":
        return True  # Si no es "Hard Control", siempre es válido

    solo_num = 0
    palabras = direc.split(' ')
    
    for palabra in palabras:
        if palabra == "":
            continue
        if solo_numeros(palabra):
            solo_num += 1
    
    if solo_num == 0:
        return False  # Al menos una palabra debe ser un número

    for palabra in palabras:
        if palabra == "":
            continue
        anterior_mayus = False
        for caracter in palabra:
            if caracter == ".":
                break
            if es_mayuscula(caracter) and anterior_mayus:
                return False  # Dos mayúsculas consecutivas
            if es_simbolo(caracter):
                return False  # No es alfanumérico ni un punto
            anterior_mayus = es_mayuscula(caracter)

    return True  # Debe ser válido y tener al menos un número


def contar_tipo_envio(tipo):
    ccs = ccc = cce = 0
    if tipo in (0,1,2):
        ccs = 1
    elif tipo in (3,4):
        ccc = 1
    elif tipo in (5,6):
        cce = 1
    return [ccs, ccc, cce]
        
def calcular_mayor (ccs,ccc,cce):
    mayor = ""
    
    if ccs >= ccc and ccs >= cce:
        mayor = "Carta Simple"
        
    elif ccc >= ccs and ccc >= cce:
        mayor = "Carta Certificada"
    
    else:
        mayor = "Carta Expresa"
    return mayor

def calcular_porcentaje(cont, ac):
    if ac != 0:
        porc = (cont *100) /ac
        porc = int(porc)
    else:
        porc = 0        
    return porc

def calcular_promedio(cont, ac):
    if ac != 0:
        prom = ac / cont
        prom = int(prom)
    else:
        prom = 0        
    return prom

def es_numero(caracter):
   # Devuelve True si el caracter es un número, de lo contrario False.

    numeros = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    return caracter in numeros

def es_letra(caracter):
    return es_mayuscula(caracter.upper())


def es_mayuscula(caracter):
    # Devuelve True si el caracter es una letra mayúscula, de lo contrario False.

    mayusculas = (
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'Á', 'É', 'Í', 'Ó', 'Ú', 'Ñ', 'Ü', 'Â', 'Ê', 'Ô', 'Ã', 'Õ', 'Ç'
    )
    return caracter in mayusculas

def solo_numeros(palabra):
    for caracter in palabra:
        if caracter == ".":
            break
        if not es_numero(caracter):
            return False
    return True


def es_simbolo(caracter):
    if es_letra(caracter) or es_numero(caracter):
        return False
    else: 
        return True


def eliminar_espacios(cadena):
    texto = ""
    for palabra in cadena:
        if palabra == " ":
            continue
        texto += palabra 
    return texto

print(eliminar_espacios("    hola mundo       "))