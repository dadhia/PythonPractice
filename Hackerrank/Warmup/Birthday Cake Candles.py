
def birthdayCakeCandles(n, candles):
    tallest = -1
    count = 0
    for i in range(n):
        if candles[i] > tallest:
            tallest = candles[i]
            count = 1
        elif candles[i] == tallest:
            count +=1

    return count


n = int(input().strip())
candles = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, candles)
print(result)
