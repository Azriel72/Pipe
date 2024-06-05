import sys

def contador(n):
    ''' Esta funcion imprime los números del 1 al n, y al final imprime un salto de línea '''
    for i in range(1, n + 1):
        print(i)
        if i == n:
            print("\n")

if len(sys.argv) != 2:
    print("Debe ingresar : 'python contador_pipe.py <número>'")
    sys.exit(1)

try:
    n = int(sys.argv[1])
    contador(n)

except ValueError:
    print("El argumento debe ser un número entero")
    sys.exit(1)
