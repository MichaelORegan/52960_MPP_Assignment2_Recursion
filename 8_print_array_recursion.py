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