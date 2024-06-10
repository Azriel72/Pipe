# This code squares numbers from 1 to n and prints a newline at the end.

import sys

def power(n):
    """ This function squares numbers from 1 to n and prints a newline at the end. """
    return n * n
    

if __name__ == "__main__":
    for line in sys.stdin:
        try:
            if line.strip() == '':
                print("\n")
                break
            number = int(line.strip())
            result = power(number)
            print(result)
        except ValueError:
            print("Please enter an integer.")
