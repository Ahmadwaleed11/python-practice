class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class student(employee):
    def __init__(self,name,id,lang):       
     super().__init__(name,id)
     self.lang=lang

obj1=employee("waleed",12)
obj2=student("waleed33",123,"python")
print(obj2.name)
print(obj2.id)
print(obj2.lang)