class a:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"name:{self.name}")

class b:
    def __init__(self,name,clas):
     a.__init__(self,name)
     self.clas=clas
     
    def show(self):
     a.show(self)
     print(f"class:{self.clas}")
class w(a,b):
   def __init__(self,name,clas,roll):
    a.__init__(self,name)
    b.__init__(self,name,clas)
    self.roll=roll

e=w("waleed",12,3)
e.show()     


