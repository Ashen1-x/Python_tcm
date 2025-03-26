#can store multiple values in one variable
#cant be ordered & dont allow duplicate values


set1 = {"a", "b", "c"}
print(set1)
print(type(set1))

set2 = {"a", "b", "c"}
print(set2)
print(len(set2))

set3 = {"a", 0, True}
print(set3)

#different way to declare a set
set4 =set(("b", 1, False))
print(set4)

set1.add("d")
print(set1)

#true is == to 1 and false is == to 0 so these are duplicates
set3.update(set4)
print(set3)


list1 = ["a", "b", "c"]
set4 = {4, 5, 6}
print(list1)
print(set4)

set4.update(list1)
print(set4)


set5 = {4, 5, 6}
set6 = set4.union(set4)
print(set6)

set4.remove(4)
print(set4)

#if the above 41 & 42 lines are called again it will bring up an error 


set4.discard(4)
print(set4)

set4.discard(4)
print(set4)
#only use pop when you dont care about the order of the data/will produce different variables each run
print(set1)
set1.pop()
print(set1)
