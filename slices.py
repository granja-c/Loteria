list1 = [1, 2, 3, 4, 5]
list2 = list1[0:3]
list3 = list1[3:len(list1)]
list4 = list2 + list3
print("Is list4 the same as list1?", list1 == list4)
print(list4)

strHello = "Hello, world!"
subStr = strHello[0:5]


print(list3)
print(subStr)
print(strHello[-1])
print(strHello[-6:-1])