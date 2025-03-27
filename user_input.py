test = input()
print(test)

test = input("Enter text here: ")
print(test)

while True:
    test = input("enter text here: ")
    print(">>> {}".format(test))
    if test == "exit":
        break
    else:
        print("....")