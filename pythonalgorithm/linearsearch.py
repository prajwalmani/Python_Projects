'''
Linear Search in python 
'''
import random
arr=[]
def linearsearch(list,key):
    for i in range(len(list)):
        if list[i]== key:
            return i
            break
    return -1

for i in range(10):
    arr.append(random.randrange(0,100))
print(arr)
key=random.randrange(0,100)
print("The key element" ,key)
res=linearsearch(arr,key)
if res==-1:
    print("element not found")
else:
    print("element found at poisition ",res)