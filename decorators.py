def greek(fx):
 def inner( *args,**kwargs):
  print('good morining')
  fx(*args,**kwargs)
  print('goodbye')
 return inner
@greek
def add(a,b):
 print(a+b)

# @greek
# def hello():
#  print('hello world')
add(2,3)