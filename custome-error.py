salary=int(input('enter the salary:'))
# if(salary=='quit'):
#     print('byy')

if(salary<100 or salary>500):
    raise ValueError('salary should be between 100 to 500')
print(salary)

