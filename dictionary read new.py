f = open('book.txt','r')
worddic = {} #empty dictionary
allwords = []
for line in f:
    newline = line.strip()
    newline = newline.split()
    allwords.extend(newline)
    
wordfreq = {}    
for word in allwords:
    try:
        wordfreq[word] = wordfreq[word] +1
    except:
        wordfreq[word] = 1
print(wordfreq)
    
    
    
    
    
    
    
    
    
    
    
'''
for x in range(len(allwords)): #for loop that repeats for every word in the list
    newline[x] = newline[x].lower() #turns each word into lowercase 


for x in newline: #for loop 
    count = newline.count(x) #counts how many times each words appears
    worddic[x] = count #appends this into empty dictionary

print('\nWord','|','Frequency')
for x in worddic: #for loop, amt of loops = amount of unique words in dictionary
    print(x,"|",worddic[x]) #prints the word as x, then the amount of times it appears
'''