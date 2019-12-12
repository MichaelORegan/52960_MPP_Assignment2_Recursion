# https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/
# https://stackoverflow.com/questions/18007995/recursive-method-for-parentheses-balancing-python

def verify_brackets(n):
    if len(n) == 0:
        return True