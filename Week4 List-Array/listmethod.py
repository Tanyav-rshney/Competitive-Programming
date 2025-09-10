# #1.append-add value to the last
# list=[2,4,5]
# list.append(100)
# # list.append(100,200) #TypeError: list.append() takes exactly one argument (2 given)
# print(list)


# #2.insert-insert a element at a index value. take two argument- element and index value
# list=[1,2,3,4]
# list.insert(1,12)
# print(list)
# list.insert(100,12) #no index found,add at last position
# print(list)


# #3.extend-add a list to a list at the last
# list=[1,2,3,4,4,5]
# print(list)
# list.extend([4,"abc",5])
# print(list)


# #4.remove-remove given element
# list.remove(3)
# print(list)


# #5.pop-remove last value by default.or can take index value
# list.pop() 
# print(list)
# list.pop(2) #can take index value
# print(list)


# #6.reverse
# list.reverse()
# print(list)
# mylist=reversed(list)
# print(mylist)


# #7.split-change every element into string,work only on space
# a="hello how are you"
# print(a.split())
# b="hello-everyone how-are-you"
# print(b.split())
# num="1234"
# print(num.split())
# num="1 2 3 4"
# print(num.split())


a=list(map(int,input().split()))
print(a)
a=map(int,input().split())
print(a)
