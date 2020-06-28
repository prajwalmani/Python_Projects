'''
Fibonacci series using Dynaiic Programming in python
'''
def fib(n):
    fibarr=[0,1]
    while len(fibarr)<n+1:
        fibarr.append(0)
    if n<=1:
        return n
    else:
        if fibarr[n-1]==0:
            fibarr[n-1]=fib(n-1)
        if fibarr[n-2]==0:
            fibarr[n-2]=fib(n-2)
    fibarr[n]=fibarr[n-1]+fibarr[n-2]
    return fibarr[n]
print(fib(2))