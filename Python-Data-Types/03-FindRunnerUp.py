if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = sorted(arr, reverse=True) 
    for i in arr:
        if i < arr[0]:
            print(i)
            break