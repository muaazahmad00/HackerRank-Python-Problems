# Enter your code here. Read input from STDIN. Print output to STDOUT

n,m = map(int,input().split())

if n % 2 != 0 and n >= 1:
    m = n * 3
    for i in range(0,int(n / 2)):
        pattern = '.|.' * ((i * 2) + 1)
        print(pattern.center(m,'-'))
    print('WELCOME'.center(m,'-'))

    for j in range(int(n /2 ), 0, -1):
        pattern = '.|.' * ((j * 2) - 1)
        print(pattern.center(m,'-'))