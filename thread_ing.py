import time
import threading

def func(seconds):

    print("hello")
    time.sleep(seconds)
# func(3)    
# func(4)    
# func(2)    
    
a1=threading.Thread(target=func,args=[2])    
a2=threading.Thread(target=func,args=[3])    
a3=threading.Thread(target=func,args=[4])    

a1.start()
a2.start()
a3.start()