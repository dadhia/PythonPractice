
n = int(input().strip())
scores = [int(score) for score in input().strip().split()]
lowestScore = scores[0]
highestScore = scores[0]
highChanges = 0
lowChanges = 0
for i in scores:
    if i > highestScore:
        highestScore = i
        highChanges += 1
    elif i < lowestScore:
        lowestScore = i
        lowChanges += 1
print("%d %d" % (highChanges, lowChanges))
