# python

■ 딕셔너리 써야 될 때
뭔가를 list로 인덱싱해서 반환하고 그럴 때가 아니라 그냥 Key값으로 찾고 싶을 때

■ set 써야될 때
뭐랑 뭐를 A∩B, A∪B, A-B해야될 때

■ List Comprehension
# list1의 x에 대해서 g(x)를 해 달라. 근데 x가 홀수이면
[g(x) for x in list1 if int(x) % 2 == 1]