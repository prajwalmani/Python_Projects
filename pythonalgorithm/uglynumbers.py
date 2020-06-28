'''
Ugly numbers in python using Dynamicc Programming
'''
def getuglyno(n):
    ugly=[0]*n
    multiple_2=2
    multiple_3=3
    multiple_5=5
    i2=i3=i5=0
    ugly[0]=1
    for i in range(1,n):
        ugly[i]=min(multiple_2,multiple_3,multiple_5)
        if ugly[i]==multiple_2:
             i2+=1
             multiple_2=ugly[i2]*2
        if ugly[i]==multiple_3:
             i3+=1
             multiple_3=ugly[i3]*3
        if ugly[i]==multiple_5:
             i5+=1
             multiple_5=ugly[i5]*5

    return ugly[-1]
print(getuglyno(150))