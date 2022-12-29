A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

b = []
for i in range(len(A)):
    if A[i] >= 50:
        b.append(A[i])

print(b)
c = 0
for i in range(len(b)):
    c += b[i]

print(c)