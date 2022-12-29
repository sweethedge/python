user_input = input('숫자를 입력하십쇼:')
numbers = user_input.split(',')
total = 0

for i in numbers:
    total += int(i)

print(total)