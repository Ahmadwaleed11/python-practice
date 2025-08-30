class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show(self):
        print(f"the name of employee is {self.name} and its id is {self.id}")    
class manger(employee):
    def info(self):
        print("hello")

obj=employee("waleed",12)      
obj.show()
obj1=employee("ahmad",121)      
obj1.show()
obj2=employee("harry",112)      
obj2.show()
obj3=manger("harryed",1122)      
obj3.show()
obj3.info()
