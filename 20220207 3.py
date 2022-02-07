x = [3, 5, 7, 8, 9, 3]
print(x[-2])

A = list(map(int, input().split()))
print(A)

A = []
for i in range(5):
    x = int(input())
    A.append(x)
    print(A)

A = [3, 5, 7, 8, 9, 12]
for i in range(len(A)):
    print(A[i], end= ' ')

A = [3, 5, 7, 8, 9, 12]
for y in A:
    print(y, end= ' ')