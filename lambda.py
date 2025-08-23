# def sum(a,b):
#     add= a+b
#     print(add)
# sum(3,6)

# div=lambda a,b: a/b
# add = lambda a,b: (a+b)*2
# print(add(2,3))
# print(div(2,2))

cube=lambda x:x*x*x
def fun(value,fx):
    return 6 + fx(value)  ######## funtion inside funtion
print(fun(3,cube))