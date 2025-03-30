#exception is an error that occurs during execution that usually represents some runtime problem that results
#   in a halt to normal execution

print(1)


#catchall statement
try:
    f = open("file.txt")
except:
    print("the file does not exist")



#prints actual problem
try:
    #asdfasdfasdf  <--- can run junk. uncomment and delete the rest of this line and see what happens
    f = open("file.txt")
except FileNotFoundError:
    print("the file does not exist")
except Exception as e:
    print(e)
finally:
    print("this message!")


n = 100 #try with 0 and "a"
if n == 0:
    raise Exception("n can't be 0!")
if type(n) is not int:
    raise Exception("n must be an int!")

print(1/n)



#Assertion hard error checking

n = 1
assert(n != 0)
print(1/n)

