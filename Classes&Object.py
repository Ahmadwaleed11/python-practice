class student:
    name='ahmad'
    rollno=23
    def info(self):
        print(f"{self.name} and its roll no is {self.rollno}")
  
a=student()
b=student()
a.name='waleed'  ###### if we want to change value
a.rollno=45
# print(a.name , a.rollno)  
a.info()
b.info()
