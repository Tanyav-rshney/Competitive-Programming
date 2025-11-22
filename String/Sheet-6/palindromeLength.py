# given a string calculate the length of longest palindromic substring
#example a b a c  a b
        #  a b a = 3
        #  a c a = 3
        #  b a c a b = 5


s = input()
max_len = 0

for i in range(len(s)):
    for j in range(i, len(s)):
        palindrome = s[i:j+1]
        if palindrome == palindrome[::-1]:  # palindrome check
            if len(palindrome) > max_len:
                max_len = len(palindrome)

print(max_len)

# given a no n and index i, print ith width of n
# n=13
# i=2
# output-1