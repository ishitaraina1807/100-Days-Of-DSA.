List = [1, 2, 4, 5, 5]
k = len(List)

i = 0
while i < k:
    j = i + 1
    while j < k:
        if List[i] == List[j]:
            removed_element = List.pop(j)
            k = k - 1
        else:
            j += 1
    i += 1

print(k)





