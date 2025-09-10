# given an array and a target find no of occurence of target no in the array


arr = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target number: "))


count = 0
for i in range(len(arr)):
    if arr[i] == target:
        count += 1

print( count)
