
def round_grades(raw_grades):
    # first mod the grade
    for i in range(len(raw_grades)):
        if raw_grades[i] < 38:
            continue
        closest = raw_grades[i] % 5
        if closest == 4:
            raw_grades[i] += 1
        elif closest == 3:
            raw_grades[i] += 2
    return rawGrades


n = int(input().strip())
rawGrades = [int(input().strip()) for i in range(n)]
finalGrades = round_grades(rawGrades)
print("\n".join(map(str, finalGrades)))

