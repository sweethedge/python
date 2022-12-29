infile = open('sample.txt')
openfile = [line.rstrip() for line in infile]

sum = 0
avg = 0
for i in range(len(openfile)):
    sum += eval(openfile[i])
    avg = sum / len(openfile)


# print(sum)
# print(avg)


