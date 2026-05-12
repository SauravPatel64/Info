
"""
14) Spiral Number Square
     1   2   3   4
    12  13  14   5
    11  16  15   6
    10   9   8   7


"""

n = int(input("Enter size: "))

arr = [[0] * n for _ in range(n)]

top = 0
bottom = n - 1
left = 0
right = n - 1
num = 1

while True:

    for i in range(left, right + 1):
        arr[top][i] = num
        num += 1
    top += 1

    if top > bottom:
        break

    for i in range(top, bottom + 1):
        arr[i][right] = num
        num += 1
    right -= 1

    if left > right:
        break

    for i in range(right, left - 1, -1):
        arr[bottom][i] = num
        num += 1
    bottom -= 1

    if top > bottom:
        break

    for i in range(bottom, top - 1, -1):
        arr[i][left] = num
        num += 1
    left += 1

for row in arr:
    for val in row:
        print(f"{val:3}", end=" ")
    print()