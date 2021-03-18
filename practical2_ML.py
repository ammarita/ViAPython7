#2.1. Working overtime hours – function:
#Rewrite your pay computation with 1.75 for overtime and create a function called
#computesalary which takes two parameters ( hours and rate):
#Enter Hours: 45
#Enter Rate: 10
#Pay: 487.50
#EXAMPLE: 487.50 = 40 * 10 + 5 * 17.5

error_message = 'Error, please enter valid numeric input!'

while True:
    hours = input('Enter Hours: ')
    try:
        hours = float(hours)
        break
    except:
        print(error_message)

while True:
    rate = input('Enter Rate: ')
    try:
        rate = float(rate)
        break
    except:
        print(error_message)
    
hours = float(hours)
rate = float(rate)

def compute_salary (hours, rate):
    pay = hours * rate
    if hours > 40:
        pay = (pay + (hours - 40) * rate * 1.75)
    return pay

print ('Pay: ', compute_salary(hours, rate))


#2.2. Using loop(s) and conditional statement(s) in Python:
#Write a program code to draw a rectagle built from thirty two * and four <space> (i.e. ‘ ‘)
#characters inside the visualization. The program code for drawing should be done in such a
#way that at each moment only one character is worked on (i.e. length one) – i.e. incoporate
#loop(s) in your code. The visualization should look like this:
# ******
#********
#**** ****
#**** ****
#********
# ******

asterix_count = 32
whitespace_count = 4
row_count = 6

def draw_rectagle(asterix, whitespace, row):
    line_length = int((asterix + whitespace + 12) / row)

    for i in range(row):
        line = ''
        for j in range(line_length):
            if((i == 0 or i == 5) and j < line_length - 1 and j > 2):
                line += '*'
            if((i == 1 or i == 4) and j < line_length and j > 1):
                line += '*'
            if(i == 2 or i == 3):
                if(j < (line_length / 2 - 1) or j > (line_length / 2)):
                    line += '*'
                else:
                    line += ' '
            j += 1
        i += 1
        print(line.center(int(line_length)))

draw_rectagle(asterix_count, whitespace_count, row_count)