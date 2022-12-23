if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input()
    m = list(student_marks[query_name])
    average = sum(m)/len(m)
    print("{:.2f}".format(average))
