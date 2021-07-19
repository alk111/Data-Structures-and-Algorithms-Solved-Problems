#Write a program to reverse an array or string

'''1) Initialize start and end indexes as start = 0, end = n-1 
    2) In a loop, swap arr[start] with arr[end] and change start and end as follows : 
    start = start +1, end = end – 1
'''

def reverselist(list1,start,end):
    while start<end:
        list1[start],list1[end]=list1[end],list1[start]
        start=start+1
        end=end-1
list1=[1,2,3,4,5,6]
print(list1)
reverselist(list1,0,5)
print(list1)
