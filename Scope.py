x = 25

def my_func():
    x = 50
    return x

print(x)

print(my_func())

print(x)


#LOCAL
lambda x:x**2

#Enclosing function locals
name = 'This is a global name'


def greet():
    #name = 'sammy'

    def hello():
        print("hello "+name)

    hello()

greet()
print(name)

y = 50

def func(y):
    print('y is ',y)
    y = 1000
    print('local y is changed to ',y)


func(y)
print(y)
