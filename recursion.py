
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial (4))    

# 4 * factorial(3)
# 4 * 3 * factorial(2)
# 4 * 3 * 2 * factorial(1)
# 4 * 3 * 2 * 1



def febo(n):
    if(n==0 or n==1):
        return n
    else:
        return febo(n-1)+febo (n-2)
print(febo(6))    
print(febo(5))    
print(febo(8))    
