name = "neut"
print(name)

name_length = 4
print(name_length)

name, name_length = "neut", 4

print(type(name))
print(type(name_length))

name_length = "4"
print(type(name_length))

name_length = int("4")
print(type(name_length))

#python is case sensitive

##important takeaway from this is variable assignment

########Diff data types###########

###List data type###

name_list = ["neut", "247CTF", "asd"]
print(type(name_list))
print(name_list)


    ##assigns the value from each index in name_list to a variable
    # name1, name2, name3 = name_list
    # print(name1)  
    # print(name2)
    # print(name3)

###Tuple###

name_tuple = ("neut", "247CTF")
print(type(name_tuple))
print(name_tuple)


###Dictionary###

name_dictionary = {"neut": 4, "247CTF": 6}
print(type(name_dictionary))
print(name_dictionary)

###Boolean###

    #True or False
name_boolean = False
print(type(name_boolean))
print(name_boolean)


###range###

name_range = range(6)
print(type(name_range))
print(name_range)


###Bytes###

name_bytes = b"neut2"
print(type(name_bytes))
print(name_bytes)

