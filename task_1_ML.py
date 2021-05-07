#1.1. Working hours – gross pay:
#Write a program to prompt the user for hours and rate per hour to compute gross pay. For
#example:
#Enter Hours: 35
#Enter Rate: 3.75
#Pay: 131.25

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
pay = float(hours) * float(rate)

print('Pay: ', pay)

#1.2. Working above hours:
#Rewrite your pay computation to give the employee 1.75 times the hourly rate for hours
#worked above 40 hours. For example:
#Enter Hours: 45
#Enter Rate: 10
#Pay: 487.50
#EXAMPLE: 487.50 = 40 * 10 + 5 * 17.5

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')

hours = float(hours)
rate = float(rate)

if hours > 40:
  pay = 40 * rate + (hours - 40) * rate * 1.75
else:
  pay = hours * rate

print ('Pay: ', pay)

#1.3. Pay program using try and except:
#Rewrite your pay program using try and except so that your program handles non-numeric
#input gracefully. For example:
#Enter Hours: 30
#Enter Rate: nine
#Error, please enter numeric input
#Enter Hours: forty
#Error, please enter numeric input

error_message = 'Error, please enter walid numeric input!'

hours = input('Enter Hours: ')

while True:
  try:
    hours = float(hours)
    break
  except:
    print(error_message)
    hours = input('Enter Hours: ')

rate = input('Enter Rate: ')

while True:
  try:
    rate = float(rate)
    break
  except:
    print(error_message)
    rate = input('Enter Hours: ')

hours = float(hours)
rate = float(rate)

if hours > 40:
  pay = 40 * rate + (hours - 40) * rate * 1.75
else:
  pay = hours * rate

print ('Pay: ', pay)