#reverse each word individually in a string
# n=input()
# reversed_s=n[::-1]
# print(reversed_s)

# #reverse the order of the word
str1=str(input())
str2=str1.split()
str2.reverse()
print("".join(str2))