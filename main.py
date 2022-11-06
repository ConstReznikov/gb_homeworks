list_of_strings = []
new_list = []
len_of_list = int(input('please enter the length of list (number): '))

for x in range(len_of_list):
    list_of_strings.append(input('enter a new string: '))

print(list_of_strings)

print('startint to sort list...')

for x in list_of_strings:
    if len(x) <= 3:
        new_list.append(x)

print('new sorterd list')

print(new_list)
