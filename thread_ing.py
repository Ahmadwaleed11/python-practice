import time
# import threading

def func(seconds):

    print("hello")
    time.sleep(seconds)
time1=time.perf_counter()
func(3)    
func(4)    
func(2)    
time2=time.perf_counter()
print(time2-time1)
    
# a1=threading.Thread(target=func,args=[2])    
# a2=threading.Thread(target=func,args=[3])    
# a3=threading.Thread(target=func,args=[4])    

# a1.start()
# a2.start()
# a3.start()