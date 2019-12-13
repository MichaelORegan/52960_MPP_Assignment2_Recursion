# 4. Remove all even numbers Given an array of numbers return an array with all the even numbers removed.

# amended from odd_numbers_recursion.py
#define function and pass array through function
def remove_even(n):
# if not an array return empty array
    if not n:
        return []
    else:
# if 1st element of array n is not divisible by 2 
        if n[0] % 2 == 1:
# return the odd number and check the array from position 1 (2nd element)
            return [n[0]] + remove_even(n[1:])
# return the array with even numbers removed
    return remove_even(n[1:])

n = [1,2,3,4,5,6,7,8,9,10]
print(remove_even(n))