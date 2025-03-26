valid = True
not_valid = False
print(valid, ",", not_valid)

#compares valid to true
print( valid == True)
print(not_valid == True)
print(valid != True)
print(not_valid != True)

print(not valid)
print(not not_valid)

print("-" *20)
#for these below you do not have to put '==True' at the end
print((10<9) == True)
print(10<9)
print((10 == 10) == True)
print((10 != 10)== True)
print((10>=10) == True)
print((10<=10) == True)
print((10> 9)) == True

print("-" * 20)

print(10 > 5 and 10 < 5)
print(10 > 5 or 10 < 5)


print(bool(0) == False)
print(bool(1) == True)

print(bool(0))
print(bool(1))

print(10 + 10)
print(10-10)
print(10/10)
print(10//10)

print(10 / 3)
print(10 // 3)
print(10 * 10)
print(10 ** 10)
print(10 % 10)

x = 10
print(x)
x = x + 1
print(x)
x += 1
print(x)
x -= 1
print(x)
x *= 5
print(x)
x /= 5
print(x)

print("-" * 20)

x = 13
print(bin(x))
#below will rmeove the "0b" before binary
print(bin(x)[2:].rjust(4,"0"))

y = 124
print(bin(y)[2:].rjust(4,"0"))

#comparing the bits for x and y
print(bin(x & y)[2:].rjust(4,"0"))
print(x & y)

#shifting bits, can shift << or >>
print(bin(x >> 1)[2:].rjust(4,"0"))

print(bin(x << 1)[2:].rjust(4, "0"))