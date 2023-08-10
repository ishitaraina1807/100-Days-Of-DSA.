flowerbed = [1, 0, 0, 0, 0, 0, 1]
n = 3
q = 0
i = 0

while i < len(flowerbed):
    if flowerbed[i] == 0:
        if (flowerbed[i+1] == 0 and flowerbed[i-1] == 0):
            flowerbed[i] = 1
            q += 1
    i += 1

if n <= q:
    print("true")
else:
    print("false")
