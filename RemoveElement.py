List = [3, 6, 7, 5, 1, 5, 2, 1]
k = len(List)

i = 0
val = 1
while i < k:
        if List[i] == val:
            removed_element = List.pop(i)
            k = k - 1
        else:
            i += 1

print(k)
print(List)





