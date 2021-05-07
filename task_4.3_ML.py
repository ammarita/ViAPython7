letter_dictionary = dict()
letter_list_to_sort = list()

# file to open: test.txt
file_name = input('Enter file name: ')
try:
    file_name = open(file_name, encoding='utf8')
except FileNotFoundError:
    print('File cannot be opened:', file_name)
    exit()

for line in file_name:
    line = ''.join(filter(str.isalpha, line)).lower()

    words = line.split()
    for word in words:
        for letter in word:
            if letter not in letter_dictionary:
                letter_dictionary[letter] = 1
            else:
                letter_dictionary[letter] += 1

for k, v in letter_dictionary.items():
    letter_list_to_sort.append((v, k))

print(sorted(letter_list_to_sort, reverse=True))