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


# try:
#       num=int(input('enter the index:'))
#       a=[6,7,3,4,5,2,4]
#       print(a[num])
# except ValueError:
#       print('invalid value')      
# except IndexError:
#       print('invalid index') 



#######  finally ##########

def fun():
   try:
      l=[2,3,4]
      i=int(input('enter the index:'))
      print(l[i])
      return 1
   except:
    print('invalid index') 
    return 0

   finally:
    print('done') 

#    print('hello')
x=fun()      
print(x)
    
    


   