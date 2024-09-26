f = open("C:\\Users\\19RMcClean.ACC\\Documents\\mynumbers.txt",'r')
user_list = f.read()

#for line in f:
#    line.split(" ")
    

def Mean(l):
    return (sum(l))/(len(l))

def Median(L):
    return L[round(len(L)/2)]
    

#print('Enter the length of your list')
#length = int(input())
#print('Enter your sorted list 1 by 1')
#user_list = [int(input()) for x in range(length)]

numwhich = int(input("""1) Mean
2) Median
"""))
if numwhich == 1:
    print(Mean(user_list))
    
if numwhich == 2:
    print(Median(user_list))



    

    
