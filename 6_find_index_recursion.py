# define function with an array the number you want to find the index of and the starting index
def find_index(n, number, index):
# index starts at 0 if first position of the array is the number return 0
    if n[0] == number:
        return index
    else:
# counting up the index as you move through the array
        index = index +1
        return find_index(n[1:], number, index)

# simple array
a = [1, 3, 4, 2, 5, 6]
# print statement, index starts at 0
print(find_index(a, 6, 0))