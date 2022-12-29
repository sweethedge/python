infile = open('abc.txt')
openfile = [line.rstrip() for line in infile]
infile.close()
openfile.reverse()

with open('reversed.txt', 'w') as f:
    for i in openfile:
        f.write(i + '\n')
