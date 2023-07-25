List = [1, 3, 7]
target = 2
i = 0
k = len(List)
ind = -1
while i < k:
    if List[i] == target:
        ind = i
        break
    else:
        if List[i] < target:
            ind = i + 1
    i = i + 1

print(ind)
