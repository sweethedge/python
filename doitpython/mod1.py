def add(a, b):
    return a + b


def sub(a, b):
    return a - b


# 이 파일을 직접 실행하면 밑에 게 실행되는데, 다른 데에서 import하면 그럴 일이 없을 거다. (211p)
if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))
