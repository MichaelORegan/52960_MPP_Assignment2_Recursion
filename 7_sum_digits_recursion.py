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