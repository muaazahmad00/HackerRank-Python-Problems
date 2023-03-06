# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import atan, degrees
AB = int(input())
BC = int(input())

angleMBC = atan(AB/BC)
print((round(degrees(angleMBC))),chr(176),sep='')
