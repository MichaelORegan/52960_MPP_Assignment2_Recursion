#1. Sum of an array Given an array of numbers return it’s sum (all the numbers added together).

# https://www.geeksforgeeks.org/sum-array-elements-using-recursion/
# amended code from above website

# defining the function
def sum_array(n):
    # base case if the array is only 1 number return that number
    if len(n)==1:
        return n[0]
    else:
        # or else return the first element in the array plus call the function on the rest of the array
        # it goes back to the base case if the array is now empty return 0 or else return the first element plus call the function
        return n[0] + sum_array(n[1:])
# simple array
a = [1, 3, 4, 2, 5, 6]
# print statement
print(sum_array(a))

b = [10, 5]
print(sum_array(b))

c = [10]
print(sum_array(c))

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

# 3. Remove all odd numbers Given an array of numbers return an array with all the odd numbers removed.

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


# 5. Replace a given character with ’*’ Given a string, and a character to replace, return a string where each occurance of the character is replaced with ’*’.

# https://stackoverflow.com/questions/38731503/recursively-replace-characters-in-string-using-python

def replacechar(string, char, replace):
    if string == "":
        return ""
    if string[0] == char:
        return replace + replacechar(string[1:], char, replace)
    return string[0] + replacechar(string[1:], char, replace)

print(replacechar('Missisippi', 'i', '*'))


# # 6. Find index in array for item. Given an array, and an element to search for return the index of the element in the array or -1 if the element is not present in the array.

# https://stackoverflow.com/questions/28056906/how-to-split-up-123456789-into-individual-numbers-using-python
# define function that passes in a number
def sum_digits(num):
# base case, if single digit return the number
    if num <= 9:
        return num
    else:
# modulus of any number by 10 is the right most digit
        return num%10 + sum_digits(num//10)

print(sum_digits(15))
print(sum_digits(8))
print(sum_digits(10))
print(sum_digits(123456789))


# 7. Sum of Digits Given a whole, number such as 23, return the sum of the digits in the number i.e. 2 + 3 = 5. For this would be useful to convert the number to a string then break it apart into digits.

# https://stackoverflow.com/questions/28056906/how-to-split-up-123456789-into-individual-numbers-using-python
# define function that passes in a number
def sum_digits(num):
# base case, if single digit return the number
    if num <= 9:
        return num
    else:
# modulus of any number by 10 is the right most digit
        return num%10 + sum_digits(num//10)

print(sum_digits(15))
print(sum_digits(8))
print(sum_digits(10))
print(sum_digits(123456789))


# 8. Print an array Given an array of integers prints all the elements one per line. This is a little bit diﬀerent as there is no need for a ’return’ statement just to print and recurse.

# define the function and pass an array to it
def print_array(n):
# setting a base case when nothing in the array return True
    if len(n) == 0:
        return True
# else print the first element (position zero), 
# recursively move through the array to print it all
    else:
        print(n[0])
        print_array(n[1:])

# simple array
a = (1,2,3,4,5)
# call to the function
print_array(a)


# 9. Find the minimum element in an array of integers. You can carry some extra information through method arguments such as minimum value.


def min_int(n):
    if len(n) == 1:
        return n[0]
    else:
        return min(n[0], min_int(n[1:]))

a = (1, 3, 4, 2, 5, 6)

print(min_int(a))

b = (2,3,4,5,6,1)
print(min_int(b))