opening_list = ["(", "{", "["]
closing_list = [")", "}", "]"]
s = "(){}"

my_list = list(s)

i = 0
j = 0
return_val = True

while j < len(my_list):
    if my_list[j] == opening_list[i] and my_list[j + 1] == closing_list[i]:
        i += 1
        j += 2
    else:
        return_val = False
        break

if return_val:
    print(True)
else:
    print(False)
