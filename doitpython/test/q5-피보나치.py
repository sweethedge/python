a = [0, 1]


def fibo(n):
    for i in range(n - 2):
        b = a[i] + a[i + 1]
        a.append(b)


fibo(8)