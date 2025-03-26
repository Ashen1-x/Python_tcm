###Tuples###

#tuples- can store multiple items in a single variable. immutable and cannot be changed.
#fixed data that is not going to change

tuple_items = ("item1", "item2", "item3")
print(tuple_items)
print(type(tuple_items))


tuple_numbers = (1, 2, 3)
print(tuple_numbers)
print(type(tuple_numbers))

print("-" * 50)

tuple_repeat = ('Combine!',) * 4
print(tuple_repeat)
print(type(tuple_repeat))


mixed_tuple = ("A", 1, ("A", 1))

print(mixed_tuple)
print(type(mixed_tuple))

#below code wont work because you cannot add to tuples
#tuple_items.append("item4")

tuple_combined = tuple_items + tuple_numbers
print(tuple_combined)
print(type(tuple_combined))

print("-" * 50)

#unpacks the items
item1, item2, item3 = tuple_items
print(item1)
print(item2)
print(item3)

#can check if something is in the tuple
print("item2" in tuple_items)
print("item3" in tuple_items)
print("item4" in tuple_items)

#can check where the index is for something. index starts at 0
print(tuple_items.index("item2"))

print(tuple_items[0])

print(len(tuple_items))

print(tuple_items[-1])
print(tuple_items[-2])

print("-" * 50)

#[including, but excluding]
print(tuple_items[0:2])
print(tuple_items[:2])
print(tuple_items[-3:-1])




#below just shows more example of playing with the index
string1 = "I am a string!"
print(string1[0:4])
print(string1[-1])

