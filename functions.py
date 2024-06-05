
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

    tiene_numero = False
    valido = True
    palabras = direc.split(' ')

    for palabra in palabras:
        if palabra == "":
            continue

        anterior_mayus = False
        for caracter in palabra:
            if caracter.isupper() and anterior_mayus:
                valido = False  # Dos mayúsculas consecutivas
            if not caracter.isalnum() and caracter != ".":
                valido = False  # No es alfanumérico ni un punto
            if caracter.isdigit():
                tiene_numero = True
            anterior_mayus = caracter.isupper()

    # Debe ser válido y tener al menos un número
    return valido and tiene_numero


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

