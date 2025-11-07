# reverse a string usin recursion
def ros(s):
    if len(s) == 0:
        return ""
    return s[-1] + ros[::-1]
