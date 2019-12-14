# 2. Product of an array Given an array of numbers return it’s product (all the numbers multiplied together).

# ammended from sum_array_recursion

# defining the function
def recursive_product(n):
# base case if the array is only 1 number return that number
    if len(n) == 1:
        return n[0]
    else:
# or else return the first element in the array multiplied by call the function on the rest of the array
# it goes back to the base case if the array is now empty return 1 or else return the first element muliplied by call the function
        return n[0] * recursive_product(n[1:])

# simple array
a = [2, 3, 4, 5]
# print statement
print(recursive_product(a))
b = [10, 5]
print(recursive_product(b))
c = [10]
print(recursive_product(c))