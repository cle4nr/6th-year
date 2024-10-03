valid = [1,2,3,4]
choosing = True
while choosing:
    menukey = int(input('''1) Create a new User ID
2) Change a password
3) Display all user IDs
4) Quit
'''))
    if menukey in valid:
        choosing = False


    


choosing2 = True
if menukey == 1:
    f=open('Passwords.csv','r')
    f.readline()
    data = []
    for line in f:
        data.append(line)

    a=open('Passwords.csv','a')
        
    while choosing2:
        newuser = input('Enter a new User ID: ')
        if newuser in userid:
         #   print('User ID already exists, Try again.')
        
        else:
            choosing2 = False
            a.write('\n')
            a.write(newuser)
            a.close()
        
    
        

'''
a = open('Books.csv','a')
for x in range(howmany):
    newline = []
    
    name = (input('Input name of book: '))
    author = (input('Input name of author: '))
    year = (input('Input year released: '))
    name = name + ', '
    author = author + ', '
    newline.append(name)
    newline.append(author)
    newline.append(year)
    a.write('\n')
    for x in newline:
        a.write(x)
'''