#python has standard functions for creating, reading, and writing files

#f = open('file.txt')
#print(f)


#f = open('file.txt', 'rt') # second argument is the mode
#print(f)



#print(f.read())

a = open('_numbers.py', 'rt')
#print(a.read())
print(a.readlines())
print(a.readlines())
#if we call a.readlines() again it will return an empty list
# a.seek(0) will fix this
a.seek(0)

print(a.readlines())
a.seek(0)

#can strip for each line in file
for line in a:
    print(line.strip())

a.close()

print("-" * 25)
#creating a file
a = open("test.txt", "w") 
a.write("test line!")
a.close()

#to append use a
a = open("test.txt", "a")
a.write("test line!")
a.close()


print(a.name)
print(a.closed)
print(a.mode)

print("-" * 25)


#for larger files you can use the fileobject as an iterator
with open('bigtextfile.txt', encoding= 'latin-1') as a:
    for line in a:
        pass
