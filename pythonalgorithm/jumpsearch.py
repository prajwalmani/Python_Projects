'''
 Jump Search in python
'''
import math
def jumpsearch(list,n,x):
    step=math.sqrt(n)
    prev=0
    while list[int(min(step,n)-1)]<x:
        prev=step
        step+=math.sqrt(n)
        if prev>=n:
            return -1
    while list[int(prev)]<x:
        prev+=1
        if prev==min(step,n):
            return -1
    if list[int(prev)]==x:
        return prev
    return -1
list=[ 0, 1, 1, 2, 3, 5, 8, 13, 21,
    34, 55, 89, 144, 233, 377, 610 ]
x = 4
n = len(list)
res=jumpsearch(list,n,x)
if res==-1:
    print("element  not found")
else:
    print('element found at poisiton',res)