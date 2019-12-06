# amended from odd_numbers_recursion.py
def remove_even(n):
    if not n:
        return []
    else:
        if n[0] % 2 == 1:
            return [n[0]] + remove_even(n[1:])
    return remove_even(n[1:])

n = [1,2,3,4,5,6,7,8,9,10]
print(remove_even(n))