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
#print('  '.join(headers)) #prints header before data
        
# for x in range (len(nowhitespace)): #for each group of data loop
#      print(*nowhitespace[x],sep='	') #* removes [''] from list

data = {}
for i in range(len(nowhitespace)):
    if int(nowhitespace[i][0]) not in data:
        data[int(nowhitespace[i][0])] = [float(nowhitespace[i][3])]
    else:
        data[int(nowhitespace[i][0])].append(float(nowhitespace[i][3])) #dictionary is only taking last piece of data in file, not all
print()
print(f"{'Duration':10s} {'Average Calories':10s}")
for duration in sorted(data):
    print(f"{duration:^10}{averagecals(data[duration]):10.1f}") #:.1f puts float to 1 decimal place, :10 makes it max 10 digits long(fills rest with white space)
        

        
#for types 45 and 60 show average of top 20 and bottom 20
    #compare values to eachother and get percentage difference

avgbot20_45 = averagecals(sorted(data[45][:20]))
avgtop20_45 = averagecals(sorted(data[45][-20:]))
avgbot20_60 = averagecals(sorted(data[60][:20]))
avgtop20_60 = averagecals(sorted(data[60][-20:]))
print()
print(f"{'Duration':7s}   {'AvgTop20-Cals':7s}   {'AvgBot20-Cals':7s}   {'Overall Average':7s}")
print(f"{'45':^8}{avgtop20_45:10.1f}  {avgbot20_45:15.1f}   {averagecals(sorted(data[45])):17.1f}")  #fix centring with cormac at home
print(f"{'60':^8}{avgtop20_60:10.1f}  {avgbot20_60:15.1f}   {averagecals(sorted(data[60])):17.1f}")  

     
    
# print(f'\nAverage top 20, Duration 45: {avgtop20_45:.1f}')
# print(f'Average bottom 20, Duration 45: {avgbot20_45:.1f}')
# print(f'Average top 20, Duration 45: {avgtop20_60:.1f}')
# print(f'Average bottom 20, Duration 45: {avgbot20_60:.1f}')



