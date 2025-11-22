#reverse a string using recursion.
def string(s):
    if len(s)==0:
        return ""
    return string(s[1:]) + s[0]
s=input()
print(string(s))