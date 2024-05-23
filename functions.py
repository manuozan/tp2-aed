
import os

def procesar_timestamp(timestamp):
    primer_caracter = ""
    for char in timestamp:

        if char == "H" or char == "S":
            primer_caracter = char

        elif char == "C":
            if primer_caracter == "S":
                return "Soft Control"
            if primer_caracter == "H":
                return "Hard Control"

    return

def clear_console():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Linux y macOS
    else:
        os.system('clear')


def procesar_direccion(direc, control):
    palabras = direc.split(' ')
    valido = True


    if control == "Hard Control":

        for palabra in palabras:
            anterior_mayus = False
            dos_mayus = False
            solo_num = True
            alfanumerico = True

            
            if palabra != "":
                for caracter in palabra:
                    

                    if caracter.isupper() and anterior_mayus:
                        dos_mayus = True
                        valido = False
                    anterior_mayus = caracter.isupper()

                    if not caracter.isdigit() and caracter != ".":
                        solo_num = False
                        
                    if not caracter.isalpha() and not caracter.isdigit() and caracter != ".":
                        alfanumerico = False
                        valido = False
        
    return valido

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
        porc = cont *100 /ac
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
