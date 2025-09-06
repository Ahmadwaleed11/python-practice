class student:
    name='ahmad'
 
    def __len__(self):
        return len(self.name)
std=student()        
print(std.name)
print(len(std))