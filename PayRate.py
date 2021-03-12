title = input('What is your job title: ')  #the name of your title
worked = input('Enter Hours: ') #number of hours you worked
hours = float(worked)
worked = input('Enter Rate: ') #enter your payrate
rate = float(worked)
if hours > 40: #if you worked more than 40 hours you will get time and a half
    pay = hours * rate + (hours - 40) * rate * 1.5
else:
    pay = hours * rate #your pay is displayed
print('Pay:', pay)
input("Press Enter to Exit") #press enter to close the command prompt
