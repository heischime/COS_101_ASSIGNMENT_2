number = [13, 21, 6, 7, 90]

okpa_list = [
    'bambara nut',
    'maggie',
    'palm oil',
    'vegetable oil',
]

okpa_list.append('fish')

print(okpa_list)



number_list = [5, 12, 8, 20, 15, 3, 7, 10, 9, 11]

total_sum = 0
for number in number_list:
    total_sum += number

print('The numbers are:', number_list)
print('The sum is', total_sum)


reversed_list = []
for i in range(len(number_list) -1, -1, -1):
    reversed_list.append(number_list[i])

print('The reversed list is:', reversed_list)


hausa_dictionary = {
    'seriki': 'king',
    'chokalie' : 'spoon',
    'zo': 'come',
    'bara' : 'rat',
}

print(hausa_dictionary['zo'])



