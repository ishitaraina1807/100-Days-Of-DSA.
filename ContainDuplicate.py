List = [1,1,1,3,3,4,3,2,4,2]
i = 0
j = i+1
n = len(List)
while i < n :
    if List[i] == List[j] :
        print("true")
        break
    else:
        print("false")
        break
i += 1
j += 1
    
