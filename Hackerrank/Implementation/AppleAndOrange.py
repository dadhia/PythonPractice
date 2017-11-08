import sys

def solveApples(s, t, a, dValues):
    count = 0
    for i in dValues:
        if a + i >= s and a + i <= t:
            count += 1
    return count


# get the input
s, t = input().strip().split()
s = int(s)
t = int(t)
a, b = input().strip().split()
a = int(a)
b = int(b)
m, n = input().strip().split()
m = int(m)
n = int(n)
apples = list(map(int, input().strip().split()))
oranges = list(map(int, input().strip().split()))

print(str(solveApples(s, t, a, apples)))
print(str(solveApples(s, t, b, oranges)))