# class employee:
#     company="apple"
#     def __init__(self,employee):
#         self.employee=employee
#     def show(self):
#         print(f"the name of employee is {self.employee} and the name of company is {self.company}")
#     @classmethod
#     def changecomp(self):
#            self.company="google" 
# e1=employee("harry")        
# e1.show()
# e1.changecomp()
# e1.show()
# print(employee.company)





class Employee:
  def __init__(self,name,salary):
   self.name=name
   self.salary=salary
  @classmethod
  def show(cls,string):
    name,salary=string.split('-')
    return cls(name,salary)
    # return cls(string.split('-')[0],string.split('-')[1])
 

e1=Employee("ahmad",1200)   
print(e1.name)
print(e1.salary)

string="ahmad-239"
e2=Employee.show(string)
print(e2.name)
print(e2.salary)

