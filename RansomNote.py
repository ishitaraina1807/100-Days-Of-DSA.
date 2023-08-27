note = "aa"
magazine = "aab"
n = note.split()
m = magazine.split()
i = 0
j = 0

while i < len(n) :
    if n[i] == m[j]:
        print("true")
    else:
        print("false")
    i += 1

    
