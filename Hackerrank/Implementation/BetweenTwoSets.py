
def find_gcd(B):
    answer = B[0]
    for i in range(1, len(B)):
        answer = gcd(answer, B[i])
    return answer


# using euclids algorithm
def gcd(a, b):
    if b > 0:
        return gcd(b, a % b)
    return a     # gcd(a, 0) = a


def find_lcm(A):
    answer = A[0]
    for i in range(1, len(A)):
        answer = answer * A[i] / gcd(answer, A[i])
    return answer


n, m = input().strip().split()
n, m = [int(n), int(m)]
A = [int(inputValue) for inputValue in input().strip().split()]
B = [int(inputValue) for inputValue in input().strip().split()]
lcm = find_lcm(A)
gcd = find_gcd(B)
i = lcm
count = 0
while i <= gcd:
    if gcd % i == 0:
        count += 1
    i += lcm
print(str(count))
