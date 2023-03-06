# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
s,k = input(),input()
patter = re.compile(k)
m=patter.search(s)

if not m:
        print((-1,-1))  
while m:
    print((m.start(),m.end()-1))
    m=patter.search(s,m.start()+1)