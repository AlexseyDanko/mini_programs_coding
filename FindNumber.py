def find_all_extra_num(list_numbers):
    count_dict = {}

    for num in list_numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    extra_num = []

    for num, count in count_dict.items():
        if count == 1:
            extra_num.append(num)

    return extra_num


list_numbers = [1.5,1, 2, 3, 4, 10, 5, 4, 3, 2, 1]
extra_num = find_all_extra_num(list_numbers)
print(extra_num)
