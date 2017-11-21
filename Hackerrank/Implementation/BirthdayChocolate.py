
def main():
    # read input
    n = int(input().strip())
    values = list(map(int, input().strip().split()))
    d, m = input().strip().split()
    d = int(d)
    m = int(m)
    result = solve(n, values, d, m)
    print(result)


# n - 2
# 12 - 2 = 10
def solve(n, values, d, m):
    num_ways = 0
    for i in range(n + 1 - m):
        total = 0
        for j in range(m):
            total += values[i + j]
        if total == d:
            num_ways += 1
    return num_ways


if __name__ == "__main__":
    main()