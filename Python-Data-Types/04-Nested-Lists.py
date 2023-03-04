if __name__ == '__main__':
    scores = []
    students = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        scores.append(score)
        students.append([name, score])
        
    scores = set(scores)
    scores = sorted(scores)
    students = sorted(students)
    
    for name, score in students:
        if score == scores[1]:
            print(name)
