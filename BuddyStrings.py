s = 'aa'
goal = 'aa'
k = list(s)
q = list(goal)
i = 0
while i < len(k):
    j = i + 1
    while j < len(k):
        k[i], k[j] = k[j], k[i]
        if k == q:
          print("true")
          break
        else:
            print("false")
            break
        j += 1
    i += 1

