# 1.Sum of list elements

A = list(map(int, input().split()))
total = 0
for i in A:
    total += i
print("Sum:", total)


#  2.Copy the Array
#  You are given a constant array A and an integer B.
#  You are required to return another array where Arr[i] = A[i] + B

A = list(map(int, input().split()))
B = int(input("Enter integer:"))
Arr = []
for i in A:
    Arr.append(i + B)
print(Arr)


#  3.Max and Min of an Array
Array = list(map(int, input().split()))
print("max:", max(Array))
print("min:", min(Array))



# 4. Search Element
# Check if B is present in A
A = list(map(int, input().split()))
B = int(input("enter search element:"))
found = 0
for i in A:
    if i == B:
        found = 1
        break
print(found)

# 5. Negative Integers
A = list(map(int, input().split()))
negatives = []
for i in A:
    if i < 0:
        negatives.append(i)
print(negatives)

# 6. Even Odd Elements
# Absolute difference between count of even & odd
A = list(map(int, input().split()))
even= 0
odd= 0
for i in A:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("difference:" ,(even- odd))

# 7. Separate Odd and Even
A = list(map(int, input().split()))
odd= []
even = []
for i in A:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Odd Elements =", odd)
print("Even Elements =", even)

# 8. Square of Array
A = list(map(int, input().split()))
B = []
for i in A:
    B.append(i * i)
print("Square =", B)

# 9. Cube of Array
A = list(map(int, input().split()))
B = []
for i in A:
    B.append(i * i * i)
print("Cube =", B)

# 10. Reverse Array (using for loop)
A = list(map(int, input().split()))
rev = []
for i in range(len(A)-1, -1, -1):
    rev.append(A[i])
print("Reverse =", rev)

# 11. Add two list elements
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
result = []
for i in range(len(A1)):
    result.append(A1[i] + A2[i])
print(result)



# 12. Find the output :
list= [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print(list[:])        # Prints entire list
print(list[::])       # prints entire list
print(list[2:5])      # From index 2 to 4 => [6,8,10]
print(list[2:])       # From index 2 to end
print(list[2::])      # From index 2 to end
print(list[:2])       # From start to index 1
print(list[::2])      # Every 2nd element
print(list[1::2])     # Every 2nd element starting from index 1
print(list[2:10:2])   # From index 2 to 9 with step 2


# 13. Find the output :
list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

print(len(list))          # Length of list
print(list[-2:-5:-1])     # Reverse slice
print(list[-2:])          # Last 2 elements
print(list[-2::])         # Same as above
print(list[:-2])          # All except last 2
print(list[::-2])         # Reverse with step 2
print(list[::-1])         # Reverse list


# 14. Find the output :
mylist = [1.4, 2, 3, 4, 5, 'Suyash']
print("Q14 Output:")
mylist.reverse()     # Reverses the list in-place
print(mylist)
print()  # Line break

# 15. Find the output (String split examples):
print("Q15 Output:")
s = "Hello everyone how are you"
print(s.split())  # Split by spaces
s = "Hello-everyone-how are you"
print(s.split("-"))  # Split by "-"
word = 'Suyash:Chaudhary:Noida'
print(word.split(':'))  # Split by ":"
t = "23456"
print(t.split())  # No delimiter given, default = space
t = "2345"
print(t.split())
print()  # Line break

# 16. Find the output :
print("Q16 Output:")
l1 = [1, 2, 3, 5, 8, 9]
l2 = [3, 4, 5, 6, 7, 10]
result = l1 + l2       # Concatenates lists
print(result)
result1 = l1 * 3       # Repeats the list 3 times
print(result1)
