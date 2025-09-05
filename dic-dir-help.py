# x=(1,2,3,4)
# print(dir(x))

class student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.roll=34
obj=student('ahmad',34)  
# print(help(student))
print(obj.__dict__)
   

