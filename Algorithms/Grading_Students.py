def gradingStudents(grades):
    res = []
    
    for grade in grades:
        if grade >= 38:
            mod5 = grade % 5

            if mod5 >= 3:
                grade += (5 - mod5)

        res.append(grade)
    return res
