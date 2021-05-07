domain_names = dict()
domains = list()

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
    email = words[1]
    domain = email.split('@')
    domains.append(domain[1])

mail_list.close()

for domain in domains:
    domain_names[domain] = domain_names.get(domain, 0) + 1

print(domain_names)