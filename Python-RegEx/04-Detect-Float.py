# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())

def is_float(s):
    pattern = r'^[-+]?(\d*\.\d+|\d+\.\d*)([eE][-+]?\d+)?$'
    return bool(re.match(pattern, s))

for i in range(n):
    s = input()
    b = is_float(s)
    print(b)