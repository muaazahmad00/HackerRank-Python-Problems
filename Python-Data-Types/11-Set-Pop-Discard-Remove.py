n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    command = input()

    if command == 'pop':
        s.pop()
    elif command[:6] == 'remove':
        s.remove(int(command[-1]))
    elif command[:7] == 'discard':
        s.discard(int(command[-1]))

print(sum(s))
    