def averagecals(calories):
    sumcal = sum(calories)
    avgcal = sum(calories) / len(calories)
    return avgcal

f = open('Exercise.csv', 'r') #open in read mode
head = f.readline() #removes header
nowhitespace = [] #empty list
for line in f:
    line = line.strip() #removes white space
    line = line.split(',') #turns each line into a list
    if '' not in line: #if it has all the data (no blanks)
        nowhitespace.append(line) #add the list of data to the empty list

for l in nowhitespace: #for loop amt of lists
    l = [float(x) for x in l] #list comprehension?? idk ignore for now


headers = head.split(',')
print('  '.join(headers)) #prints header before data
        
for x in range (len(nowhitespace)): #for each group of data loop
    print(*nowhitespace[x],sep='	') #* removes [''] from list
data = {}

for i in range(len(nowhitespace)):
    if nowhitespace[i][0] not in data:
        data[int(nowhitespace[i][0])] = [float(nowhitespace[i][3])]
    else:
        data[int(nowhitespace[i][0])].append(float(nowhitespace[i][3]))
print()
print(f"{'Duration':10s} {'Average Calories':10s}")
for duration in sorted(data):
    print(f"{duration:^10}{averagecals(data[duration]):10.1f}") #:.1f puts float to 1 decimal place, :10 makes it max 10 digits long(fills rest with white space)
        

        
