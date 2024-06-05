direc = "Los Andes 2024."
control = "Hard Control"

def procesar_direccion(direc, control):
    if control != "Hard Control":
        return True  # Si no es "Hard Control", siempre es válido

    palabras = direc.split(' ')
    for palabra in palabras:
        if palabra == "":
            continue

        anterior_mayus = False
        for caracter in palabra:
            if caracter.isupper() and anterior_mayus:
                return False  # Dos mayúsculas consecutivas

            if not (caracter.isalpha() or caracter.isdigit() or caracter == "."):
                return False  # No es alfanumérico ni un punto

            anterior_mayus = caracter.isupper()
    
    return True  # Si no se encontró ningún problema, es válido

print(procesar_direccion(direc, control))