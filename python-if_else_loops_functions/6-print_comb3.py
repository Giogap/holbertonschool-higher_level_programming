#!/usr/bin/python3
cont = 0;
j = 0
for i in range(0, 8):
    cont = cont + 1
    j = cont
    for j in range (j, 10):
        if i != j:
            print("{}{}".format(i, j), end=", ")
print("89")
