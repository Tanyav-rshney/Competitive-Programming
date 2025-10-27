# #print all the values of subarray
# arr = [1, 2, 3]

# for i in range(len(arr)):
#     for j in range(i, len(arr)):
#         print(arr[i:j+1])


# #given an array find the sum of all subarryas
# # Given array
# arr = [1, 2, 3]

# print("Subarrays and their sums:")

# for i in range(len(arr)):
#     for j in range(i, len(arr)):
#         sub = arr[i:j+1]        # subarray
#         s = sum(sub)             # sum of that subarray
#         print(sub, "=> Sum =", s)




# #given an array find the sum of all subarryas sums
# arr = [1, 2, 3]
# n = len(arr)
# total = 0

# for i in range(n):
#     total += arr[i] * (i + 1) * (n - i)

# print("Sum of all subarray sums:", total)



# #given an integer array num, find the subarray with the largest sum
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# max_sum = nums[0]
# current_sum = 0

# for num in nums:
#     current_sum = max(num, current_sum + num)
#     max_sum = max(max_sum, current_sum)

# print("Largest subarray sum:", max_sum)



