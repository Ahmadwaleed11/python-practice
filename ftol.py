from functools import lru_cache
import time
@lru_cache(maxsize=None)
 

def fx(n):
    time.sleep(3)
    return(n*3)

print(fx(2))
print('hello')    
print(fx(3))
print('hello')    
print(fx(4))
print('hello')   

print(fx(2))
print('hello')
print(fx(3))
print('hello')
print(fx(4))
print('hello')