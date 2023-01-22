def letter(score):
    score *= 2
    grades = [(9, 'A+'), (8.5, 'A'), (8, 'A-'), (7.5, 'B'), (7, 'B-'), (6.5, 'C'), (6, 'D'), (0, 'F')]
    for i in range(len(grades)):
        if score >= grades[i][0]:
            return grades[i][1]