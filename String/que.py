# you have give string s and you have to find all amazing substrings of s, an amazing substring is one that starts with a vowel 
#input A B E C
#output 6




#find no of occurence of bob of string a consisiting of lowercase english alphabets
#A='abobc'
#'bob'
A = input("Enter a string: ")
count = 0

for i in range(len(A) - 2):
    if A[i:i+3] == "bob":
        count += 1

print("Number of occurrences of 'bob':", count)


#  Akash likes playing with strings. One day he thought of applying following operations on the
#  string in the given order:
#  Concatenate the string with itself.
#  Delete all the uppercase letters.
#  Replace each vowel with '#'.
#  You are given a string A of size N consisting of lowercase and uppercase alphabets. Return the
#  resultant string after applying the above operations.
#  NOTE: 'a' , 'e' , 'i' , 'o' , 'u' are defined as vowels.
#  Input:
#  A="aeiOUz"
#  Output:
#  "###z###z"

A = input()
A = A + A
B = ""

for ch in A:
    if not ('A' <= ch <= 'Z'):
        B = B + ch

for v in "aeiou":
    B = B.replace(v, "#")

print(B)

