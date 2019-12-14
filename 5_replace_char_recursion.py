# 5. Replace a given character with ’*’ Given a string, and a character to replace, return a string where each occurance of the character is replaced with ’*’.

# https://stackoverflow.com/questions/38731503/recursively-replace-characters-in-string-using-python

# define function string and the character we want to replace and the character we want in its place
def replace_char(string, char, replace):
# if it is an empty string
    if string == "":
# return nothing
        return ""
# if the zeroth/first element is the character
    if string[0] == char:
# put the replace character in its place and call the function on the rest of the string
        return replace + replace_char(string[1:], char, replace)
# return the altered string with the replaced characters
    return string[0] + replace_char(string[1:], char, replace)

print(replace_char('Missisippi', 'i', '*'))