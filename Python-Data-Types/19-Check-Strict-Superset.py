# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(map(int, input().split()))
n = int(input())
result = 'True'
for i in range(n):
    sett = set(map(int, input().split()))
    if A.issuperset(sett):
        result = 'True'
    else:
        result = 'False'
        break
print(result)
    