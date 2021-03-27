ratings = ''
title = ''

cereals = open('cereals.csv', 'r')
cereals.readline()

for line in cereals:
    line = line.rstrip()

    if line.startswith('"'):
        title += str(line.split('"')[1]) + ' '
    else:
        title += str(line.split(',')[0]) + ' '

    last_comma = line.rfind(',')
    ratings += line[last_comma + 1 : len(line)] + ' '

cereals.close()

min_rating = float(ratings.split(' ')[0])
max_rating = float(ratings.split(' ')[0])
mean_rating = 0
i = 0
min_index = 0
max_index = 0

while i < 16:
    rating_to_check = float(ratings.split(' ')[i])

    if(rating_to_check < min_rating):
        min_rating = rating_to_check
        min_index = i

    if(rating_to_check > max_rating):
        max_rating = rating_to_check
        max_index = i

    mean_rating += rating_to_check

    i += 1

mean_rating /= 15

print('The lowest cereals rating value: ' + str(min_rating) + ' Cereals name: ' + title.split(' ')[min_index])
print('The average cereals rating value: ' + str(mean_rating))
print('The highest cereals rating value: ' + str(max_rating) + ' Cereals name: ' + title.split(' ')[max_index])
