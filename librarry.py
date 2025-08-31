class library:
    def __init__(self,num ,name):
        self.booknum=num
        self.bookname=name
    def show(self):
        print(f"there are {self.booknum} books in library and its name is {self.bookname}")
    def check(self):
        if self.bookname!=self.booknum:
            print("book is not available")
        else:
            print("book is available")

lib=library(2,"python")
lib.show()    
lib.check()          