n = int(input())
k = 0
while n!=0:
    k = k+1
    n = int(input())
print(k)

n = int(input())
k = 0
while n!=0:
    k = k+n
    n = int(input())
print(k)

n = int(input())
k = 0
s = 0
while n!=0:
    k = k+1
    s = s+n
    n = int(input())
print(s/k)

n = int(input())
k = 0
while n!=0:
    if n % 2 ==0:
         k = k + 1
    print("k=", k)
    n = int(input())

n = int(input())
Max = 0
while n!=0:
    if n > Max:
        Max = n
    n = int(input())
print(Max)

