# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    s = input()
    if re.search(r'<[a-zA-Z][\w\-.]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>', s):
        print(s)