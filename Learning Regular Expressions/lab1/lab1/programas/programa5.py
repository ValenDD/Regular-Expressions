import re
import sys

def prog(texto):
    match = re.findall(r'"tag": "(.*)",\n\s*"patterns": \[\s*((?:"([^"]*)",?\s*)+)\],\n\s*"responses": \[\s*((?:"([^"]*)",?\s*)+)', texto)
    tags = patterns = responses = 0
    for i in match:
        tags += 1
        patterns += len(re.findall(r'"(.*)",?',i[1]))
        responses += len(re.findall(r'"(.*)",?',i[3]))
    separator = ' '
    return f"{str(tags)+separator+str(patterns)+separator+str(responses)}"

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
