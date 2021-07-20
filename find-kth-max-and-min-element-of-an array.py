def kthmin(a,k):
    a.sort()
    return a[k-1]
def kthmax(a,k):
    a.sort()
    return a[-k]
a=[1,2,3,4,5,6]
k=3
print("kth min element :",kthmin(a,k))
print("kth max element :",kthmax(a,k))

