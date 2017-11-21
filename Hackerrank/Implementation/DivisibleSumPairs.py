
def main():
    n, k = input().strip().split(' ')
    n = int(n)
    k = int(k)
    a = list(map(int, input().strip().split(' ')))
    result = divisible_sum_pairs(n, k, a)
    print(result)


def divisible_sum_pairs(n, k, a):
    pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (a[i] + a[j]) % k == 0:
                pairs += 1
    return pairs


if __name__ == "__main__":
    main()
