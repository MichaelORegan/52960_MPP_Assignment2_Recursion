# https://stackoverflow.com/questions/38731503/recursively-replace-characters-in-string-using-python

def replacechar(string, char, replace):
    if string == "":
        return ""
    if string[0] == char:
        return replace + replacechar(string[1:], char, replace)
    return string[0] + replacechar(string[1:], char, replace)

print(replacechar('Missisippi', 'i', '*'))