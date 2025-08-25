from random import choices

print("welcome to the game")
print("what are you choosing : rock,paper,scissor")

userchoice = input('Enter your choice:')
print("your choice is ", userchoice)

computerchoice = choices(['rock','paper','scissor'])

print("computer choice is ", computerchoice)

if(userchoice=='rock' and computerchoice=='rock'):
  print('tie')
elif(userchoice=='paper' and computerchoice=='scissor'):
  print('you win')  
elif(userchoice=='scissor' and computerchoice=='paper'):
  print('you loose')  
elif(userchoice=='paper' and computerchoice=='rock'):
  print('you loose')  
elif(userchoice=='rock' and computerchoice=='scissor'):
  print('you win')  
elif(userchoice=='rock' and computerchoice=='paper'):
  print('you loose')  
elif(userchoice=='scissor' and computerchoice=='scissor'):
  print('you tie')
else:
  print('you loose')    
