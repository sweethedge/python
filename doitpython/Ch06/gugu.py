# def gugu(num):
#     for i in range(9):
#         print(num * (i + 1))

# gugu(2)

def gugu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n * i)
        i += 1
    return result


print(gugu(2))
