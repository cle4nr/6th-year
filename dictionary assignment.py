worddic = {}
sentence = input("give sentence: ")
sentence = sentence.split()

for x in range(len(sentence)):
    sentence[x] = sentence[x].lower()


for x in sentence:
    count = sentence.count(x)
    worddic[x] = count


for x in worddic:
    print(x,"|",worddic[x])
    
    

