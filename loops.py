#can loop over any iterable object you can obtain an iterator from

#unrelated. just making a function here
def divider():
    print("-" * 10)
##################################

a = 1
print(a)
a+=1
print(a)
a+=1
print(a)


#while loop
divider()

a = 1
while a < 5:
    a+=1
    print(a)
    

divider()

#for loop
for i in [0, 1, 2 , 3, 4]:
    print(i+6)
    
divider()

for i in range(5):
    print(i+6)
    
divider()
#nested loops
for i in range(3):
    for j in range(3):
        print(i, j)
        
divider()

for i in range(5):
    if i == 2:
        break
    print(i)
    
    
divider()
    
for i in range(5):
    if i == 2:
        continue
    print(i)
    
divider()
for i in range(5):
    if i == 2:
        pass
    print(i)
    
divider()
#looping string
for c in "string":
    print(c)
    
divider()
for key, value in {"a": 1, "b": 2, "c": 3}.items():
    print(key, value)
    
    
    
    

    