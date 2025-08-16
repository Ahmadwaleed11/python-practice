# for i in range(6):
#     print(i)
#     if (i==4):
#        print('helllo')
#     continue
   
# else:    
#     print('sorry')

# i=0
# while i<7:
#     print(i)
#     i=i+1
#     if (i==4):
#      print('hello')
#      continue

# a=input('enter the number:')
# print(f'multipication table of {a} is ')
# for i in range(1,11):
#     print(f"{int(a)} X {i} = {int(a)*i}" )
# print('imp line')

##### if error occur ############

# a=input('enter the number:')
# print(f'multipication table of {a} is ')
# try:
#   for i in range(1,11):
#     print(f"{int(a)} X {i} = {int(a)*i}" )
# except:    
#     print('invalid input')

# # print('imp line')


####### diff except error ######


try:
      num=int(input('enter the number:'))
      a=[6,7]
      print(a[num])
except ValueError:
      print('invalid value')      
except IndexError:
      print('invalid index')      
   