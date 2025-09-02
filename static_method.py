class student :
    def __init__(self,num):
        self.num=num
    def add(self,add):
        self.num=self.num+add
    @staticmethod
    def show(a,b): 
        return a+b      
a=student(12)        
print(a.num)

a.add(23)
print(a.num)

print(student.show(2,4))  # we eecute the static method with class also
print(a.show(2,4))       # we execute the static method with object