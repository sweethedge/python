user_input = input('���ڸ� �Է��Ͻʼ�:')
numbers = user_input.split(',')
total = 0

for i in numbers:
    total += int(i)

print(total)