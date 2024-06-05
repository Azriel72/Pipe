import sys

def potenciador():
    ''' Esta función imprime los cuadrados de los números del 1 al n, y al final imprime un salto de línea '''
    for line in sys.stdin:
        try:
            if line == '\n':
                print("\n")
                return
            number = int(line.strip())
            print(number ** 2)
        except ValueError:
            print("Favor ingresar un número entero")

potenciador()
