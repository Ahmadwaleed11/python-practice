# class student:
#    def __init__ (self,n,s):
#      self.name=n
#      self.sect=s
#    def show(self):
#        print(f"my name is {self.name } and my section is {self.sect}")
#    @property
#    def get_name(self):
#          return self.name   
# obj=student("waleed",2)
# obj.show()
# print(obj.get_name)

class student:
    def __init__ (self,value):
        self.value=value

    def show(self):
        print(f"value is {self.value}") 
    @property
    def get_value(self):
        return 10*self.value    
    @get_value.setter
    def get_value(self,new_value):
        self.value=new_value/10
    
    
obj=student(12)  
obj.get_value=23     

print(obj.get_value)  
obj.show()



