# x=4  ####### global variable

# def fun():
#     y=3          ############ local variable
#     print(y)  
   

# fun()
# print(x)
# print(y)




x=6

def func():
    global x
    x=3   ####### if we want to change global variable
    print(x)
   
    y=4
    print(y)



func()    
# print(x)
