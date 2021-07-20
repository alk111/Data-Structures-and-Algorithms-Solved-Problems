#Move all negative numbers to beginning and positive to end 
def allneg(a,b):
    for i in range(1,len(a)):
        if a[i]<0:
            b.append(a[i])
    for i in range(1,len(a)):
        if a[i]>0:
            b.append(a[i])
a=[1,2,-5,9,-3,4,-11]
b=[]
allneg(a,b)
print(a)
print(b)

        

    
