'''
Binary Search in python 
'''
import random
import sys
sys.setrecursionlimit(150000)
def binarysearch(list,l,h,key):
    if h>=1:
        mid=(h-l)//2
        if list[mid]==key:
            return mid
        elif list[mid]>key:
            return  binarysearch(list,l,mid-1,key)
        else:
            return binarysearch(list,mid+1,h,key)
    else:
        return -1

arr=arr = [ 2, 3, 4, 10, 40 ]
res=binarysearch(arr,0,len(arr)-1,10)
if res ==-1:
  print("elment not found")
else:
    print("elemet found at",res)