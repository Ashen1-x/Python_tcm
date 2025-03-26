###Lists

#unlike tuples, we can change the data for lists

list1 = ["A", "B", "C", "D", "E", "F"]
print(list1)

#different types of data we can store in a list
list2 = ["A", 1, 2.0, ["A"], [], list(), ("A"), False]
print(list2)
print(type(list2))

print(list1[0])
print(list1[-1])

#accessing a nested loop. finds the list at 3rd index, prints 0 index
print(list2[3][0])

list1[0] = "X"
print(list1)

del list1[0]
print(list1)

list1.insert(0, "A")
print(list1)

list1.append("G")
print(list1)

print(max(list1))
print(min(list1))
print(list1.index("C"))
print(list1[list1.index("C")])

list1.reverse()
print(list1)

list1 = list1[:-1]
print(list1)

print(list1.count("A"))
list1.append("A")
print(list1.count("A"))

list1.pop()
print(list1)

list3 = ["H","I","J"]
print(list3)

list1.extend(list3)
print(list1)

list1.clear()
print(list1)

#sort
list4 = [8, 2, 5, 6, 17, 2]
print("-" * 20)
print(list4)
list4.sort()
print(list4)

#reverse sort
list4.sort(reverse=True)
print(list4)

list5 = list4
print("*" * 10)
print(list4)
print("*" * 10)

print(list5)

list5[2] = "X"
print(list5)
print(list4)

list6 = list4.copy()
print(list4)
print(list6)

list6[2] = "A"
print("-" * 15)
print(list6)
print(list4)
print("-" * 15)
list7 = ["1", "2", "3",]
print(list7)

list8 = list(map(float, list7))
print(list8)
