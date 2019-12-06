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