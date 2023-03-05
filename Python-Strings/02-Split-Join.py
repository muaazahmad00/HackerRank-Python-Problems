def split_and_join(line):
    # write your code here
    splt = line.split(" ")
    joind = "-".join(splt)
    return joind
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)