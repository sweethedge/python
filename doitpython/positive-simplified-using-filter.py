def positive(x):
    return x > 0


print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

'''
이름조차 필요 없는 간단한 함수가 필요할 때 lambda
(lambda 매개변수: 리턴값, 그-함수-적용할-대상)
'''

print(list(filter(lambda x: x > 0, [1, -3, 2, -5, 6])))
