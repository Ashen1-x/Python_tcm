def function1():
    print("hello from function1")

function1()


def function2():
    return "hello from function2"

function2()

return_from_function2 = function2()
print(return_from_function2)


def function3(s):
    print("\t{}".format(s))

function3("parameter")
function3("parameter2")


def function4(s1, s2):
    print("{} {}".format(s1, s2))

function4("any", "thing")
function4(s1 = "thing", s2 = "any")
function4(s2 ="any", s1 = "thing")

def function5(s1 = "default"):
    print("{}".format(s1))

function5()
function5(s1 = "not default, haha")


#can create functions that can handle an unknown or a variable number of arguments with an *

def function6(s1, *more):
    print("{} {}".format(s1, " ".join([s for s in more])))

function6("function6")
function6("function6", "a")
function6("function6", "a", "b", "c")


def function7(**ks):
    for a in ks:
        print(a, ks[a])

function7(a ="1", b = "2", c ="3", d = "4")


def function8(s, f, i, l):
    print(type(s))
    print(type(f))
    print(type(i))
    print(type(l))

function8("string", 1.0, 1, ['l', 'i', 's', 't'])



v = 100
print(v)

def function9():
    global v
    v += 1

function9()
print(v)

def function10():
    print("hello from funciton10")

def function11():
    function10()
    print("hello from function11")

function11()

#recursion - a function calling itself
def function12(x):
    print(x)
    if x > 0:
        function12(x-1)

function12(5)

def function13(x):
    while x >= 0:
        print(x)
        x -= 1

function13(5)