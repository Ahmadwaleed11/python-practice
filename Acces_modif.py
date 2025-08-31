# class employee:
#     def __init__(self):             //// Public class 
#         self.name="harry"
   
# a=employee()        
# print(a.name)


class employee:
    def __init__(self):             
        self.__name="harry"        # private classs / can be access indirectly
   
a=employee()     
  
print(a._employee__name)

