# f=open('f3.txt', 'r')

# i=0
# while True:
#      line=f.readline()
#      i=i+1
   
#      if not line:
#         break
#      m1=line.split(',')[0]
#      m2=line.split(',')[1]
#      m3=line.split(',')[2]
#      print(f"Marks of student {i} in english:{m1}")
#      print(f"Marks of student {i} in isl:{m2}")
#      print(f"Marks of student {i} in math:{m3}")
   

########## writelines() ###########################

# f=open('f3.txt', 'w')
# lines=['12,34,56\n','32,45,76\n','67,23,22\n']
# f.writelines(lines)
# f.close

# print(f.write('2,34,56\n'))
# print(f.write('32,45,76\n'))
# print(f.write('67,23,22\n'))

######### seek() ######################



# f=open('f3.txt', 'r')

# f.seek(8) ############ move to the 8 byte of file
# print(f.tell())  ######### tell the current position
# print(f.read())



########### Truncate func ################

f=open('f3.txt', 'w')
print(f.write('hello wolrd'))
f.truncate(8)  ######### how byte we want in file ########


