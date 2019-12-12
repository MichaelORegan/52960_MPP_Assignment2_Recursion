def min_int(n):
    if len(n) == 1:
        return n[0]
    else:
        return min(n[0], min_int(n[1:]))

a = (1, 3, 4, 2, 5, 6)

print(min_int(a))

b = (2,3,4,5,6,1)
print(min_int(b))