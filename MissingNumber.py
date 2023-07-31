List = [0,1,,3, 2,4,5,6]
n = len(List)
Sum = n * (n + 1) / 2
List_sum = sum(List)
if Sum == List_sum:
    print("no missing number")
else:
    missing_number = Sum - List_sum
    print(int(missing_number))
