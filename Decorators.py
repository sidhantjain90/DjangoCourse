s = 'GLOBAL VARIABLE!'

def func():
    mylocal=10
    # print(locals())
    print(globals()['s'])

func()


def hello(name='sid'):
    print('Hello function has been run!')
    def greet():
        return "THis string is inside greet()"
    def welcome():
        return "This string is inside welcome!"
    if name == 'sid':
        return greet
    else:
        return welcome


x = hello()
print(x())


# Passing function as argument
def hello1():
    return "Hi Sid!"

def other(func):
    print("Hello ")
    print(func())

other(hello1)


#Decorators
def new_decorator(func):

    def wrap_func():
        print("Code here before executing func")
        func()
        print("Func has been called")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("This function is need of a decorator!")


# func_needs_decorator = new_decorator(func_needs_decorator)

# func_needs_decorator()


func_needs_decorator()
