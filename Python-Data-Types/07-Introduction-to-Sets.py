def average(array):
    # your code goes here
    avg = sum(set(array))/len(set(array))
    avg = round(avg, 3)
    return avg
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)