#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    fun = sys.argv
    n = len(fun)
    suma = 0
    suma = int(suma)
    for i in range(1, n):
        fun[i] = int(fun[i])
        suma = suma + fun[i]
    print("{}".format(suma))
