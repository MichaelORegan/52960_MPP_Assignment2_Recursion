# 9. Find the minimum element in an array of integers. You can carry some extra information through method arguments such as minimum value

# define function and pass an array to it
def min_int(n):
# if length of n is aqual to 1
    if len(n) == 1:
# return that single element
        return n[0]
# or else
    else:
# return minimum of first element and call the function to the next element
        return min(n[0], min_int(n[1:]))

# the function breaks down the array into pieces and then compares the elements as it puts them back together
# returning the minimum value as it puts them back together, eventually returning the minimum value in the array

a = (1, 3, 4, 2, 5, 6)

print(min_int(a))

b = (2,3,4,5,6,1)
print(min_int(b))