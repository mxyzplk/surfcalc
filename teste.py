import os
import numpy as np

f = open("cases.txt", "r")

lista2 = []

nptemp = np.empty((19), dtype="float")
npglobal = np.empty((19), dtype="float")

lista = f.readline().split()

print(lista)

Lines = f.readlines()

a = len(Lines)

casos=np.empty((a,19),dtype="float")

i = 0

for line in Lines:
    casos[i,:] = line.strip().split()
    i = i + 1

print(casos)