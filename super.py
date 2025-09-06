class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
class student(employee):
    def __init__(self,name,id,lang,ver):       
     super().__init__(name,id)
     self.lang=lang
     self.ver=ver

obj1=employee("waleed",12)
obj2=student("waleed33",123,"python","2.0")
print(obj2.name)
print(obj2.id)
print(obj2.lang)
print(obj2.ver)