class animal:
    def __init__(self,name,spec):   
        self.name=name
        self.spec=spec
    def show(self):
        print(f"name:{self.name}")    
        print(f"specie:{self.spec}")    
class dog(animal):
    def __init__(self,name,breed): 
        animal.__init__(self,name,spec="russian") 
        self.breed=breed 
       
    def show(self):
        animal.show(self)  
        print(f"breed:{self.breed}")    
class golden(dog):
    def __init__(self,name,color): 
        dog.__init__(self,name,breed="lolo") 
        self.color=color
       
    def show(self):
        dog.show(self)  
        print(f"color:{self.color}")    
o=golden("billo","black")
o.show()