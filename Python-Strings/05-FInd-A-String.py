def count_substring(string, sub_string):
    
    s_len = len(string)
    sub_len = len(sub_string)
    count = 0
    
    for i in range(s_len):
        if sub_string in string[i:sub_len+i]:
            count += 1

    return count

if __name__ == '__main__':