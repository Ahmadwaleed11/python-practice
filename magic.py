class student:
    def __init__(self,name):
        self.name=name
   
 
    def __len__(self):
        return len(self.name)
    def __str__(self):
       return(f"my name is {self.name}")
    def __call__(self):
       print("my name is ")
std=student("ahmad")        
print(std.name)
print(len(std))