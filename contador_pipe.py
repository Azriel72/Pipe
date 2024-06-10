# This code counts numbers from 1 to n and prints a newline at the end.

import sys

def counter(n):
    """ This function prints numbers from 1 to n, and a newline at the end.  """
    resultado = []
    for i in range(1, n + 1):
        if i == n:
            resultado.append(i)
            return resultado
        else:
            resultado.append(i)

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            print("Usage: python counter_pipe.py <number>")
            sys.exit(1)

        n = int(sys.argv[1])
        result = counter(n)
        for i in result:
            print(i)
    except ValueError:
        print("The argument must be an integer.")
        sys.exit(1)
