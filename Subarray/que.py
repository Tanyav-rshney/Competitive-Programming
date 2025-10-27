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
arr = [3, -2, 4, -1, 2, 6]
index = 5
n = len(arr)

# formula: (index + 1) * (n - index)
count = (index + 1) * (n - index)
print( count)
