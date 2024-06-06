from functions import *
from tp1 import *

# Llamar a la función para limpiar la consola
clear_console()

# INICIALIZACIÓN DE VARIABLES 
control = ""
cedvalid = cedinvalid = 0
imp_acu_total = 0
ccs = ccc = cce = 0
tipo_mayor = 0
primer_cp = ""
cant_primer_cp = 0
menimp = None
mencp = ""
c_r13 = ac_r13 = 0
porc = prom = 0
c_r14 = ac_r14 = 0

# Abrimos el archivo en modo lectura
m = open('envios.txt')

# Primera línea del archivo para el control
control = procesar_timestamp(m.readline().strip())

cp = direc = tipo_envio = forma_pago = ""

n = 1
while True:
    linea = m.readline()
    if linea == "": # Si no hay más líneas, salir del bucle
        break

    cp = eliminar_espacios(linea[:9])
    print(cp)
    direc = linea[9:28]
    tipo_envio = int(linea[29])
    forma_pago = int(linea[30])
    
    importe = procesar_envio(cp, direc, tipo_envio, forma_pago)[3]

    if n == 1:
        primer_cp = cp
    
    print(n, direc, procesar_direccion(direc, control))
    if procesar_direccion(direc, control):
        destino = procesar_envio(cp, direc, tipo_envio, forma_pago)[0]
        provincia = procesar_envio(cp, direc, tipo_envio, forma_pago)[1]
        cedvalid += 1
        imp_acu_total += procesar_envio(cp, direc, tipo_envio, forma_pago)[3]
        
        ccs += contar_tipo_envio(tipo_envio)[0]
        ccc += contar_tipo_envio(tipo_envio)[1]
        cce += contar_tipo_envio(tipo_envio)[2]
        tipo_mayor = calcular_mayor(ccs, ccc, cce)
        
        if destino != "Argentina":
            c_r13 += 1
            ac_r13 += 1
        else:
            ac_r13 += 1
            if provincia == "Provincia de Buenos Aires":
                ac_r14 += importe
                c_r14 += 1
    else:
        cedinvalid += 1
        destino = procesar_envio(cp, direc, tipo_envio, forma_pago)[0]
    
    if cp == primer_cp:
        cant_primer_cp += 1

    if destino == "Brasil":
        if menimp is None:
            menimp = importe
        if importe < menimp:
            menimp = importe
            mencp = cp

    n += 1

m.close()

porc = calcular_porcentaje(c_r13, n-1)
prom = calcular_promedio(c_r14, ac_r14)

print(' (r1) - Tipo de control de direcciones:', control)
print(' (r2) - Cantidad de envíos con dirección válida:', cedvalid)
print(' (r3) - Cantidad de envíos con dirección no válida:', cedinvalid)
print(' (r4) - Total acumulado de importes finales:', imp_acu_total)
print(' (r5) - Cantidad de cartas simples:', ccs)
print(' (r6) - Cantidad de cartas certificadas:', ccc)
print(' (r7) - Cantidad de cartas expresas:', cce)
print(' (r8) - Tipo de carta con mayor cantidad de envíos:', tipo_mayor)
print(' (r9) - Código postal del primer envío del archivo:', primer_cp)
print('(r10) - Cantidad de veces que entro ese primero:', cant_primer_cp)
print('(r11) - Importe menor pagado por envíos a Brasil:', menimp)
print('(r12) - Código postal del envío a Brasil con importe menor:', mencp)
print('(r13) - Porcentaje de envíos al exterior sobre el total:', porc)
print('(r14) - Importe final promedio de los envíos Buenos Aires:', prom)
