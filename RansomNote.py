note = "aa"
magazine = "aab"
magazine_counts = {}
for char in magazine:
    if char in magazine_counts:
        magazine_counts[char] += 1
    else:
        magazine_counts[char] = 1
can_construct = True
for char in note:
    if char in magazine_counts and magazine_counts[char] > 0:
        magazine_counts[char] -= 1
    else:
        can_construct = False
        break

if can_construct:
    print("true")
else:
    print("false")

