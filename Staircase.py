"""
Input Format

A single integer, , denoting the size of the staircase.

Output Format

Print a staircase of size using # symbols and spaces.
"""
n = int(input().strip())
staircase = [ ['#' if n - j < i else ' ' for j in range(1, n + 1)] for i in range(1, n + 1)]
for step in staircase:
    print("".join(step))