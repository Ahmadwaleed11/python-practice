def cube(x):
    return x*x*x
print(cube(3))

l=[2,3,4,5,6]
# newl=[]
# for item in l:
#     newl.append(cube(item))

# print(newl)  
 


newl=list(map(cube,l) )
print(newl)
