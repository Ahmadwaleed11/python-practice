class animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    def show(self):
        print(f"the name of animal is {self.name} and its spec is {self.sound}")    
class cat(animal):
    def __init__(self,name,breed):
     animal.__init__(self,name,sound="dog") 
     self.breed=breed 
    def mak_sound(self):
        print("mew") 
          
c=cat("cat","domestic")
c.mak_sound()
d=animal("dog","bark")
d.show()