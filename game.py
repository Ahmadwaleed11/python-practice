from random import choice

print('Welocme to the game')
print('what are you choosing:')
print(['rock','paper','scissor'])

userchoice=input('enter your choice:')
print('your choice is ',userchoice)

computerchoice=choice(['rock','paper','scissor'])
print('computer choice is ',computerchoice)

if(userchoice==computerchoice):
    print('tie')
elif(userchoice=='rock' and computerchoice=='scissor'):
    print('you win')
elif(userchoice=='paper' and computerchoice=='rock'):
    print('you win')
elif(userchoice=='scissor' and computerchoice=='paper'):
    print('you win')
else:
    print('you lose')