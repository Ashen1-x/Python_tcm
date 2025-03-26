string1 = "I am a string!"
print(string1)
print(type(string1))

string2 = 'I am a string too!'
print(type(string2))

string3 = """I am a
very
long 
string!
"""

print(string3)

string4 = "I\"m a string"
print(string4)

string5 = 'I\'m a string!'
print(string5)

string6 = 'I"m a string'
string7 = "I'm a string\nI\'m on a newline!"
print(string7)

string8 = "\\ \x41\x42\x43"
print(string8)

string9 = "a" * 10
print(string9)


print(len(string9))

print("string" in string4)
print("neut" in string4)

print(string4.startswith("I"))
print(string4.startswith("n"))
print(string4.index("string"))
print(string4.upper())
print(string4.lower())


messy_string = "    Messy string!  "
print(messy_string)
print(messy_string.strip())
print(messy_string.replace("!", "?").strip())
print(messy_string.replace("string", "example"))
print(messy_string.split())

string10 = "this, is, a, string!"
print(string10.split(","))
print(string10)

string11 = "I am a string!"
print(string11)
print(string11.encode())
print(string11.encode("utf-8"))

print(string11.rjust(25))
print(string11.rjust(25, "x"))
print(string11.ljust(25,"x"))
print(string11.rjust(25,"x").ljust(35,"x"))

print("I am " + "a string")
print("String 4 is " + str(len(string4)) + " characters long")
print("1" + "1")
print(type("1" + "1"))

print("string4 is {} characters long!".format(len(string4)))
print("{} {} {}".format(len(string4), 5.0, 0x12))
print("{0} {2} {1}".format(len(string4), 5.0, 0x12))
print("{length}".format(length=len(string4)))


length = len(string4)
print(f"string4 is {length} characters long")

print("string4 is {length:.2f} characters long".format(length=len(string4)))
print("string4 is {length:.4f} characters long".format(length=len(string4)))

#hex
print("string4 is {length:x} characters long".format(length=len(string4)))
#binary
print("string4 is {length:b} characters long".format(length=len(string4)))
#octal
print("string4 is {length:o} characters long".format(length=len(string4)))


print("string4 is %d characters long" % len(string4))
print("string4 is %f characters long" % len(string4))
print("string4 is %x characters long" % len(string4))


