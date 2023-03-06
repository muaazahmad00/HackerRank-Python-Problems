def merge_the_tools(string, k):
    n = len(string)
    i =0
    while i < n:
        sub_str = string[i:i+k]
        uni_char = set(sub_str)
        uni_char = []
        for ch in sub_str:
            if ch not in uni_char:
                uni_char.append(ch)
         
        print(''.join(uni_char))
        i+=k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)