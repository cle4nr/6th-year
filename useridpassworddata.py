def validpassword(passw):
    if len(passw) < 8:
            print('Too short, needs atleast 8 characters.')
            return False
    else:
        hasupper = haslower = hasnumber = hasspecial = False
        for c in passw:
            if c.isupper():
                hasupper = True
            elif c.islower():
                haslower = True
            elif c.isdigit():
                hasnumber = True
            elif not c.isalnum():
                hasspecial = True
        if all((hasupper,haslower,hasnumber,hasspecial)): #if hasupper and haslower and hasnumber and hasspecial: 
            return True
            
        else:
            if not hasupper:
                print('No uppercase letters, needs atleast 1.')
            if not haslower:
                print('No lowercase letters, needs atleast 1.')
            if not hasnumber:
                print('No numbers, needs atleast 1.')
            if not hasspecial:
                print('No special characters, needs atleast 1.')
            return False
                    

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
        data.append(line.split(', '))

    a=open('Passwords.csv','a')
        
    while choosing2:
        newuser = input('Enter a new User ID: ')
        if newuser in [user[0] for user in data]: #list comprehension to get list of users from list of users and passwords(data) 
            print('User ID already exists, Try again.')

        else:
            choosing2 = False
    choosing3 = True
    print('''Your password should have at least 8 characters
It should include upper case letters
It should include lower case letters
It should include numbers
It should include one special character !, £, $, €, %, &, *, #
''')
    while choosing3:    
        passw = input('Enter a valid password: ')
        if validpassword(passw):
            choosing3 = False
        
                    
        
            
                        
    a.write(newuser+', '+passw+'\n')
    a.close()
            
        
    
        
#for password change, use list comprehension; if newuser in [user[0] for user in data]:
#repeat function for password check, then append
#for user[0] in data print blah blah