#https://stackoverflow.com/questions/51199082/typeerror-can-only-concatenate-list-not-nonetype-to-list
#define function and pass array through function
def remove_odd(n):
# if not an array return empty array
    if not n:
        return []
    else:
# if 1st element of array n is divisible by 2 
        if n[0] % 2 == 0:
# return the even number and check the array from position 1 (2nd element)
            return [n[0]] + remove_odd(n[1:])
# return the array with odd numbers removed
    return remove_odd(n[1:])

n = [1,2,3,4,5,6,7,8,9,10]
print(remove_odd(n))