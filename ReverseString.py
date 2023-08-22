def reverseList(lst, i, j):
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1
lst = ['i', 's', 'h', 'i', 't', 'h' ,'a']
print(lst)
reverseList(lst, 0, 6)
print("Reversed list is")
print(lst)
