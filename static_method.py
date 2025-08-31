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

print(a.show(2,4))