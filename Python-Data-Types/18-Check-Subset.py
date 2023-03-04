# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

for test in range(n):
    num_A = int(input())
    A = set(input().split())
    num_B = int(input())
    B = set(input().split())
 
    if A.issubset(B):
        print("True")
    else:
        print("False")