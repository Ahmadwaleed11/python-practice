class animal:
    def __init__(self,name,spec):
        self.name=name
        self.spec=spec
    def show(self) :
        print(f"the animla is {self.name}")  

class cat(animal):
    def __init__ (self,name,spec,breed):
        animal.__init__(self,name,spec)  
        self.breed=breed
    def show(self):
        print(f"the name of animal is {self.name} and the spec is {self.spec} and the bredd is {self.breed}")





d=animal("dog","canine")        
d.show()
c=cat("cat","feline","domestic")
c.show()