#given n array elements, every element repeats twice except 1. Find the unique element
def find_unique(arr):
    ans = 0
    for num in arr:
        ans ^= num
    return ans


arr = list(map(int,input().split()))
print(find_unique(arr))




# arr = list(map(int,input().split()))

# for i in range(len(arr)):
#     count = 0
#     for j in range(len(arr)):
#         if arr[i] == arr[j]:
#             count += 1
#     if count == 1:
#         print(arr[i])
#         break

