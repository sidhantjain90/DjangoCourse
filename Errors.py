# Try, except, else...
try:
    f = open('simple.txt','r')
    f.write("Test write to simple text!")
except IOError:
    print('Error: Could not find file or read data!')
else:
    print("Success!")
    f.close()
print("Hello World!")

# Using Finally
try:
    f.open('simple.txt','r')
    f.write("Test write to simple text!")
except:
    print('Error: Could not find file or read data!')
finally:
    print("I Always Work!")
