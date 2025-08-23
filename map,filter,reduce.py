# def cube(x):
#     return x*x*x
# print(cube(3))

# l=[2,3,4,5,6]
# # newl=[]
# # for item in l:
# #     newl.append(cube(item))

# # print(newl)  
 


# newl=list(map(cube,l) )
# print(newl)


######### filter ######################

def filter_func(x):
    return x>23

l=[22,3,53,33,34,5]

newl=list (filter(filter_func,l))
print(newl)

