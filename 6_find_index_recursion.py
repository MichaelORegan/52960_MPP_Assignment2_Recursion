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