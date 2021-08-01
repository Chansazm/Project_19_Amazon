#fibonacci

def fib(n):
    #base case when n = 1
    if (n == 0):
        return 0
    elif(n == 1):
        return 0
    
    
    return fib(n-1) + fib(n - 2)
    
    #return fib
num = 9
print(fib(9))


