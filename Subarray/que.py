#print all the values of subarray
# arr=[1,2,3,4,5]

# for i in range(len(arr)):
#     for j in range(i + 1, len(arr) + 1):
#         print(arr[i:j])


# Function to print sybarray of given array
# def printSubarray(A, start, end):
#     for i in range(start, end + 1):
#         print(A[i], end=" ")
#     print()  

# def printAllSubarray(A):
#     N = len(A)
#     for i in range(N):         
#         for j in range(i, N): 
#             printSubarray(A, i, j)


# A = [1, 2, 3]
# printAllSubarray(A)



# #print sum of every single subarray
# def printSubarray(A, start, end):
#     sum=0
#     for i in range(start, end + 1):
#         sum += A[i]  
#     print(sum)

# def printAllSubarray(A):
#     N = len(A)
#     for i in range(N):         
#         for j in range(i, N): 
#             printSubarray(A, i, j)


# A = [1, 2, 3]
# printAllSubarray(A)


#given an integer array nums,find the subarray with largest sum and return total sum
# nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
# # Output=6
# nums=[5, 4, -1, 7, 8]


#given an array elements, find the sum of all subarrays
# arr = [1, 2, 3]

# print("Subarrays and their sums:")

# for i in range(len(arr)):
#     for j in range(i, len(arr)):
#         sub = arr[i:j+1]     
#         s = sum(sub)             
#         print(sub, "=> Sum =", s)



#if we know in howmany subaaray each element is coming,we can solve this problem fast
#in howmany subarray index 3 is present [3,-2, 4, -1, 2,  6]
# s=i+1
# e=n-i
# arr = [3, -2, 4, -1, 2, 6]
# index = 5
# n = len(arr)

# # formula: (index + 1) * (n - index)
# count = (index + 1) * (n - index)
# print( count)


#given an array a of n non negative and in non negative number b need to find number of sub array in a with a sum less than b
# A = [2 5 6]
# B = 10
# output = 4

# A = list(map(int, input().split()))
# B = int(input())

# count = 0
# n = len(A)

# for i in range(n):
#     s = 0
#     for j in range(i, n):
#         s += A[j]
#         if s < B:
#             count += 1
#         else:
#             break   

# print(count)


# given an array of integer A , a subarray of an array is said to be good if it fulfills anyone of the criteria:
#1. length of a subarray is to be even and sum of all elements of the subarray must be less than b 
#2. length of a subarray is to be odd and sum of all elements of the subarray must be greater than b  
#your task is to find count of good subarrays in A
# A = list(map(int, input().split()))
# B = int(input())

# count = 0
# n = len(A)

# for i in range(n):
#     s = 0
#     for j in range(i, n):
#         s += A[j]
#         length = j - i + 1

#         if (length % 2 == 0 and s < B) or (length % 2 == 1 and s > B):
#             count += 1

# print(count)

#you have given an integer array c of size a now you need to find a subarray so that the sum of continuous elements is maximum but the sum not must not exceed b
# a=3
# b=1
# c=[2, 2, 2]  output =0

# a=5
# b=12
# c=[2, 1, 3, 4, 5]  output = [3, 4, 5]


# A = int(input("Enter size of array: "))
# C = list(map(int, input("Enter array elements: ").split()))
# B = int(input("Enter maximum allowed sum: "))

# maxV = 0
# best_subarray = []
# n = len(C)

# for i in range(n):
#     s = 0
#     current = []
#     for j in range(i, n):
#         s += C[j]
#         current.append(C[j])
        
#         if s <= B and s > maxV:
#             maxV = s
#             best_subarray = current[:]
#         if s > B:
#             break

# if maxV == 0:
#     print(0)
# else:
#     print(best_subarray)


#Given an array a of length n your task is to find maximum possible sum of any non empty contiguous subarray in other words among all possible subarrays of a determine the 1 leads that the highest sum and written the sum
n = int(input("Enter size of array: "))
A = list(map(int, input("Enter array elements: ").split()))

max_sum = A[0]     
current_sum = A[0]  

for i in range(1, n):
    # either continue the current subarray or start new from A[i]
    current_sum = max(A[i], current_sum + A[i])
    
    # update max_sum if current_sum is greater
    max_sum = max(max_sum, current_sum)

print("Maximum Subarray Sum =", max_sum)
