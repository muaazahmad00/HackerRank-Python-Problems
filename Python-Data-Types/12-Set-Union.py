# Enter your code here. Read input from STDIN. Print output to STDOUT

num_A = int(input())
A= set(map(int, input().split()))

num_B = int(input())
B = set(map(int, input().split()))

print(len(A.union(B)))