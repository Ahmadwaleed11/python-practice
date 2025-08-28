class name:
    def __init__(self,n):
        self.name=n

    def show(self):
        print(self.name)   

    @property
    def info(self):
        return 5*self.name         
a=name(23)
a.show()
print(a.info)