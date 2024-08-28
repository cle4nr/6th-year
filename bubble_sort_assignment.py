def bubble_sort(lisT):
    n = len(lisT)
    for pass_ in range(n-1):
        for b_sort in range(n-1):
            if lisT[b_sort] > lisT[b_sort+1]:
                placehold = lisT[b_sort]
                lisT[b_sort] = lisT[b_sort+1]
                lisT[b_sort+1] = placehold
                
    return(lisT)



lisT = []
play = True
while play == True:
    num1 = (input("Enter next number for your list: "))
    if "*" not in num1:
        lisT.append(num1)
    else: break
                 

print(bubble_sort(lisT))
                
            
            
