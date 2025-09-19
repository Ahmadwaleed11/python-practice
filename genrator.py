def my_generator():
    for i in range(10):
     yield i
gen=my_generator()    

for k in gen:
 print(k)