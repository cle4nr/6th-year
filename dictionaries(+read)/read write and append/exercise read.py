f = open('C:\\Users\\19RMcClean.ACC\\Downloads\\Exercise.csv', 'r')
head = f.readline()
ld = []
l2 = []
for line in f:
    line = line.strip()
    line = line.split(',')
    if '' not in line:
        l2.append(line)

for l in l2:
    l = [float(x) for x in l]
    

        
print(head)

        
for x in range (len(l2)):
    print(*l2[x],sep='	')
    
    

    
