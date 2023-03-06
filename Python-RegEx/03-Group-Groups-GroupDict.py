# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

string = input()

m = re.search(r'([a-zA-Z0-9])\1+', string)

if m is not None:
    print(m.group(1))
else:
    print(-1)
