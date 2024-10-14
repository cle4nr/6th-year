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


        
print(head) #prints header before data
        
for x in range (len(nowhitespace)): #for each group of data loop
    print(*nowhitespace[x],sep='	') #* removes [''] from list
d15 = []
d20 = []
d25 = []
d30 = []
d45 = []
d60 = []
d75 = []
d80 = []
d90 = []
d120 = []
d150 = []
d160 = []
d180 = []
d210 = []
d270 = []
d300 = []

for i in range(len(nowhitespace)):
    if nowhitespace[i][0] == '15':
        d15.append(float(nowhitespace[i][3]))
    if nowhitespace[i][0] == '20':
        d20.append(float(nowhitespace[i][3]))
    if nowhitespace[i][0] == '25':
        d25.append(float(nowhitespace[i][3]))
print(averagecals(d15))
print(averagecals(d20))
print(averagecals(d25))
#     if nowhitespace[i][0] == '30':
#         d30.append(nowhitespace[i][3])
#         print(averagecals(d30))
#     if nowhitespace[i][0] == '45':
#         d45.append(nowhitespace[i][3])
#         print(averagecals(d45))
#     if nowhitespace[i][0] == '60':
#         d60.append(nowhitespace[i][3])
#         print(averagecals(d60))
#     if nowhitespace[i][0] == '75':
#         d75.append(nowhitespace[i][3])
#         print(averagecals(d75))
#     if nowhitespace[i][0] == '80':
#         d80.append(nowhitespace[i][3])
#         print(averagecals(d80))
#     if nowhitespace[i][0] == '90':
#         d90.append(nowhitespace[i][3])
#         print(averagecals(d90))
#     if nowhitespace[i][0] == '120':
#         d120.append(nowhitespace[i][3])
#         print(averagecals(d120))
#     if nowhitespace[i][0] == '150':
#         d150.append(nowhitespace[i][3])
#         print(averagecals(d150))
#     if nowhitespace[i][0] == '160':
#         d160.append(nowhitespace[i][3])
#         print(averagecals(d160))
#     if nowhitespace[i][0] == '180':
#         d180.append(nowhitespace[i][3])
#         print(averagecals(d180))
#     if nowhitespace[i][0] == '210':
#         d210.append(nowhitespace[i][3])
#         print(averagecals(d210))
#     if nowhitespace[i][0] == '270':
#         d270.append(nowhitespace[i][3])
#         print(averagecals(d270))
#     if nowhitespace[i][0] == '300':
#         d300.append(nowhitespace[i][3])
#         print(averagecals(d300))
        
 

