"""
Given five positive integers, find the minimum and maximum values that can be
calculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a single line of
two space-separated long integers.
"""

integers = input().strip().split(' ')
integers = [int(i) for i in integers]
withoutIndex = [[integers[i] for i in range(5) if i != j] for j in range(5)]
mins = [sum(withoutIndex[i]) for i in range(len(withoutIndex))]
maxs = [sum(withoutIndex[i]) for i in range(len(withoutIndex))]
minValue = min(mins)
maxValue = max(maxs)
print(str(minValue) + " " + str(maxValue))