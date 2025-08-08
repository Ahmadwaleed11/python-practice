def average(*number):
    sum=0
    for i in number:
        sum=sum+i
        print('average is ', sum/len(number))


average(2,4,5,6)
