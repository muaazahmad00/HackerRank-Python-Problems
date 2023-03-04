# Enter your code here. Read input from STDIN. Print output to STDOUT
lst = []

k = int(input())
lst = input().split()
room_count = {}

for room in lst:
    if room in room_count:
        room_count[room] += 1
    else:
        room_count[room] = 1
for room in room_count:
    if room_count[room] == 1:
        unique_room = room
        break
print(unique_room)
