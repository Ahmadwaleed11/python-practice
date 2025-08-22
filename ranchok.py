f=open('f3.txt', 'r')

i=0
while True:
     line=f.readline()
     i=i+1
   
     if not line:
        break
     m1=line.split(',')[0]
     m2=line.split(',')[1]
     m3=line.split(',')[2]
     print(f"Marks of student {i} in english:{m1}")
     print(f"Marks of student {i} in isl:{m2}")
     print(f"Marks of student {i} in math:{m3}")
   

