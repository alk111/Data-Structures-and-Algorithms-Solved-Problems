#Find the minimum and maximum element in an array using minimum comparisons
def findminmax(A):
    min=max=A[0]
    for i in range(1,len(A)):
        if A[i]< min:
            min=A[i]
        elif A[i]>max:
            max=A[i]
    print("minimum element is :",min)
    print("maximum element is :",max)
A=[5,7,3,2,9,10,]
findminmax(A)
