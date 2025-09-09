class student:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f'the name of student is {self.name}')    
class teacher:
    def __init__(self,teachername):
        self.teachername=teachername
    def show(self):
        print(f'the name of teacher is {self.teachername}')         
         
    
class college(student,teacher):
    def __init__(self,name,teachername):
        self.name=name
        self.teachername=teachername
        
obj=college("waleed","harry")  

print(obj.name)
print(obj.teachername)
obj.show()