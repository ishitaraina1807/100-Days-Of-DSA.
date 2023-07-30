def ways(n):
    if n == 2:
        return 2
    elif n == 3:
        return 3
    else:
        return ways(n - 1) + ways(n - 2)
print(ways(5))
