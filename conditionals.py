#conditionals are executed in linear order

if True:
    print("True")
    
if False: 
    print("False")
    
if not False:
    print("not False")
    
    
    
#checks if something is true    
if 1 < 1:
    print("1 < 1")
elif 1 <= 0:
    print("1 <= 1")
    
#catch all with else
else:
    print("else 1")
    
    

print("-" * 25)

if 1 <1 :
    print("1 < 1")
elif 1 < 1:
    print("1 <= 1")
elif 2 < 2:
    print("2 <= 2")
    
else:
    print("else reached")
    
    
    
print("-" * 25)

if 1 > 0 and 0 < 1:
    print("1 > 0 and 0 < 1")
    
if 1 < 0 and 0 > 1:
    print("1 < 0 and 0 > 1")
    

if (1<0 or 0 < 1) and 1 == 1:
    print("1 < 0 or 0 < 1")
    
    
        
if 0 < 1: print("0 < 1")


#inline method
print("1 >= 1" if 1 >= 1 else print("1 < 1"))
#or written like this
if 1 >= 1:
    print("1 >= 1")
else: 
    print("1 < 1")


#below is another example of two different ways to write conditionals. both ask the same thing
if 0 > 1:
    print("1")
elif 0 < 1:
    print("2")
else:
    print("3")
    
# and

print("1") if 0 > 1 else print("2") if 0 < 1 else print("3")
