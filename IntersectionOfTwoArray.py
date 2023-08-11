List1 = [1, 4, 2, 5]
List2 = [4, 2, 6]
List3 = []

for i in List1:
    for j in List2:
        if i == j:
            List3.append(j)

print(List3)
