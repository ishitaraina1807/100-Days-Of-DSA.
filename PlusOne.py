my_list = [9]
result_integer = int(''.join(map(str, my_list)))

result_integer += 1

updated_list = [int(digit) for digit in str(result_integer)]

print(updated_list)  
