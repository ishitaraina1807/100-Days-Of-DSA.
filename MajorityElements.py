List = [3,2,1,1,1,2,2]
List2 = [3,2,3]
i = 0
n = len(List2)

while i < n:
    if List2.count(List2[i]) > n / 2:
        print(List2[i])
    else:
        print("no element is repeating n/2 times")
    i += 1
    break
