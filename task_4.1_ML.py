# file to open: mbox-short.txt
line_count = 0
file_name = input('Enter a file name: ')

try:
    mail_list = open(file_name)
except FileNotFoundError:
    print('Cannot open file: ' + file_name)
    exit()

for line in mail_list:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    line_count += 1
    print(words[1])

mail_list.close()

print('Found ' + str(line_count) + ' emails')