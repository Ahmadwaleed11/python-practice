# a=234
# b=123
# print('a') if a>b else print('unless') if a==b  else print('b') 
# print(23) if a<b else ''


####### Enumerate function #########$##

# marks=[12,23,45,12,34]

# index=0
# for mark in marks:
#     print(mark)
#     if (index==2):
#      print('ahmad')
#     index=index+1

# marks=[12,23,45,12,34]
# for index,mark in enumerate(marks):
#     print(mark)
#     if (index==2):
#      print(index,mark)


fruit=['apple','banana','orange','peach']
for index,fruit in enumerate(fruit):
    print(index,fruit)
