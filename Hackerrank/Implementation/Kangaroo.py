
def kangaroo(x1, v1, x2, v2):
    # need to solve something like this: y1 = x1 + steps*v1 and y2 = x2 + steps*v2
    # x1 + steps*v1 = x2 + steps*v2
    # x1-x2 + steps(v1-v2) = 0
    if v2 >= v1:
        return False
    if (x1-x2) % (v1-v2) != 0:
        return False
    return True


x1, v1, x2, v2 = input().strip().split()
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
if result:
    print("YES")
else:
    print("NO")
