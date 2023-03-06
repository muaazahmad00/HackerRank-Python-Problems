# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(input())

def reSub(line):
    line = re.sub(r"(?<=\s)&&(?=\s)", "and", line)
    line = re.sub(r"(?<=\s)\|\|(?=\s)", "or", line)
    return line


for i in range(n):
    line = input()
    line = reSub(line)
    print(line)
