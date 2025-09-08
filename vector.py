class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"  
    def __add__(self,a):
        return vector(self.i+a.i , self.j+a.j , self.k+a.k)
      
v1=vector(2,3,4)      
print(v1)
v2=vector(23,34,42)      
print(v2)
print(v1+v2)
print(type(v1+v2))
