#https://stackoverflow.com/questions/51199082/typeerror-can-only-concatenate-list-not-nonetype-to-list
def remove_odd(n):
    if not n:
        return []
    else:
        if n[0] % 2 == 0:
            return [n[0]] + remove_odd(n[1:])
    return remove_odd(n[1:])

n = [1,2,3,4,5,6,7,8,9,10]
print(remove_odd(n))