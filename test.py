box =[]
for i in open('ted.txt', 'r').readlines():
    for a in range(100):
        i = i.strip(' '*a)
        i = i.strip('\n'*a)
    box.append(i)
print(box)