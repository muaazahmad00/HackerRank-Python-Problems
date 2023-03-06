def minion_game(string):
    v = 'AEIOU'
    stu_score = 0
    kev_score = 0
    n = len(string)
    for i in range(n):
        if string[i] in v:
            kev_score += n-i
        else :
            stu_score += n-i
    if stu_score > kev_score:
        print('Stuart', stu_score)
    elif kev_score > stu_score:
         print('Kevin', kev_score)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)