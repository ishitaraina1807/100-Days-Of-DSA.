my_list = [1, 0, 2, 0, 12]
total_no = len(my_list)
i = total_no - 1

while i >= 0:
    if my_list[i] == 0:
        my_list.pop(i)
        my_list.append(0)
    i -= 1

print(my_list)
