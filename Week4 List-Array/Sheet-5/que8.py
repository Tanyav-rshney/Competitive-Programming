list1 = [1,2,3,4,4,5]
list2 = [5,6,7,8]
result = []

for i in range(len(list2)):
    # for i in range(len(list2)):
         result.append(list1[i] + list2[i])
print(result)