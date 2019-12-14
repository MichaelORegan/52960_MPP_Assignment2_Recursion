# https://stackoverflow.com/questions/18007995/recursive-method-for-parentheses-balancing-python

# define the function, string n with (), 
# i in n start at 0, counter start at 0
def verify_parentheses(n, i=0, counter=0):
    # if there is nothing in the string 
    if i == len(n):
    # return 0 balanced True
        return counter == 0
    #if the counter is less than 0
    if counter < 0:
    # it is not balanced and return False
        return False
    # starting at positon 0 as per i's value, if this is "("
    if n[i] == "(":
    # call the function on the next position, increase i and increase the counter
        return  verify_parentheses(n, i + 1, counter + 1)
    # or if the positon 0 as per i's value, if this is ")"
    elif n[i] == ")":
    # call the function on the next position, increase i and reduce the counter
        return  verify_parentheses(n, i + 1, counter - 1)
    # return the boolean answer whether the string is balanced or not
    return verify_parentheses(n, i + 1, counter)

a = "(()()"
print(verify_parentheses(a))
b = "(()"
print(verify_parentheses(b))
c = "(())"
print(verify_parentheses(c))
d = ")(()"
print(verify_parentheses(d))
e = "())(())("
print(verify_parentheses(e))
f = "()((("
print(verify_parentheses(f))
g = ""
print(verify_parentheses(g))