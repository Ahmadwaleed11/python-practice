class math:
    def __init__(self,num):
        self.num=num
    def addtonum(self,n):
        self.num=self.num +n  
    @staticmethod
    def add(a,b):
        return a+b    
a=math(2)
print(a.num)
a.addtonum(3)
print(a.num)

print(a.add(2,3))