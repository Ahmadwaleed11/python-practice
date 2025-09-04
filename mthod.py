class employee:
    noofemployee=0
    def __init__(self,name):
        self.name=name
        self.raise_amount=34
        self.companyname="apple"
        employee.noofemployee +=1
    def show(self):
        print(f"the name of employee is {self.name} and the amount raise of company {self.companyname} for this employee is {self.raise_amount} and the employee no is {self.noofemployee}")    
emp1=employee("ahmad") 
emp1.raise_amount=45 
emp1.companyname="google"     
emp1.show()
emp2=employee("waleed")       
emp2.show()