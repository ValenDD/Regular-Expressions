import re
import sys

def prog(texto):
    #Despliega todas las intenciones (valor del campo tag) con terminación -ent, -ing, -or, u -on del archivo de entrada
    match = re.findall(r'"tag": "(.*?ent|.*?ing|.*?or|.*?on)",', texto)
    separator = ' '
    ret = separator.join(match)
    return ret

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    f = open(entrada, 'r') # abrir archivo entrada
    datos = f.read()       # leer archivo entrada
    f.close()              # cerrar archivo entrada
    
    ret = prog(datos)      # ejecutar er
    
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
