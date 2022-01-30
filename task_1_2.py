my_three_list = []
for number in range(1000):
    if number % 2 != 0:
        my_three_list.append(number**3)
print(my_three_list)

sum_of_values = 0
for element in my_three_list:
    check_sum = 0
    for check_num in str(element):
        check_sum += int(check_num)
    if check_sum % 7 == 0:
        sum_of_values += element
print(sum_of_values)

sum_of_values = 0
for element in my_three_list:
    element += 17
    check_sum = 0
    for check_num in str(element):
        check_sum += int(check_num)
    if check_sum % 7 == 0:
        sum_of_values += element
print(sum_of_values)