# Functions
def my_func(param1='default'):
    """
    THIS IS THE DOCSTRING
    """
    print("my first Python function!")

my_func()


def hello():
    return "Hello!"

result = hello()
print(result)

def addNum(num1, num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "Sorry ! I need integers!"

result1 = addNum("1","2")
print(result1)


#Lambda Expression

#Filter Functions
mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 == 0

evens = filter(even_bool,mylist)
print(list(evens))

evens = filter(lambda num:num%2==0, mylist)
print(list(evens))


tweet = "Go Sports! #Sports"
result = tweet.split("#")[1]
print(result)

# in operator

bool = 'x' in [1,2,3,'x']
print(bool)
