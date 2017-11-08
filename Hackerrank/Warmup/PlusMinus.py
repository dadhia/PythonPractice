import sys

n = int(input().strip())
arr = [int(number) for number in input().strip().split(' ')]
# counts
negative = 0
positive = 0
zero = 0
for value in arr:
    if value < 0:
        negative += 1
    elif value == 0:
        zero += 1
    else:
        positive += 1
print(str(round(positive/n, 6)))
print(str(round(negative/n, 6)))
print(str(round(zero/n, 6)))