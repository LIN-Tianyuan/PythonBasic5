number_list = [32, 5, 12, 8, 3, 75, 2, 15]
number = number_list[0]
i = 0
while i < len(number_list):
    if number < number_list[i]:
        number = number_list[i]
    i = i + 1
print('Le plus grand élément de cette liste a la valeur ' + str(number) + '.')

# for element in number_list:
#     if element >= max_number:
#         max_number = element
# print(max_number)
