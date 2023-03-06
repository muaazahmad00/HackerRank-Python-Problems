#!/bin/python3

import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

transp = "".join([matrix[j][i] for i in range(m) for j in range(n)])

ending = re.search("[^a-zA-Z0-9]*$", transp).group()[1:]
middle = re.sub("[^a-zA-Z0-9]+", " ", transp).strip()
begining = re.search("^[^a-zA-Z0-9]*", transp).group()[:-1]

rslt = ""
rslt += begining
rslt += middle
rslt += ending

print(rslt)