#used to store data values in key value pairs, cant have duplicate keys {key: value}

dict1 = {"a": 1, "b":2, "c":3}
print(dict1)
print(type(dict1))
print(len(dict1))

#same-same, but different
print(dict1["a"])
print(dict1.get("a"))

print("-" * 25)

print(dict1.keys())
print(dict1.values())
print(dict1.items())

dict1["a"] = 1
print(dict1)

dict1["d"] = 4
print(dict1)

#can change value
dict1["a"] = 0
print(dict1)

dict1.update({"a": 1})
print(dict1)

dict1.pop("d")
print(dict1)

del dict1['c']
print(dict1)

dict1['c'] = {"a": 1, "b": 2}
print(dict1)


#declare empty dictionary
dict2 = {}
print(dict2)
# or
dict3 = dict()
print(dict3)