import re
expression = ".#[0-9A-Fa-f]{3,6}"
for i in range(int(input())):
    inpt = re.findall(expression, input())
    if inpt:
        for j in inpt:
            print(j[1:])