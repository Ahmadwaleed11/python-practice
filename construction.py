class person:
    def __init__ (self,n,o):
       print("this is constructor")  
       self.name=n
       self.occ=o
    # name='ahmad'
    # occ='student'
    def info(self):
     print(f"my name is {self.name} and i am {self.occ}")   
a=person("waleeed","teacher")

a.info()