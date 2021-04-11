# Control FLow
if 1 < 2:
    print('First Block!')
    if 20 < 3:
        print('Second Block!')


if 1 > 2:
    print("Hello!")
elif 3 == 3:
    print('elif ran')
else:
    print('Last')


# For loops

seq = [1,2,3,4,5]

for item in seq:
    print(item)


d = {"Sam":1, "Frnk":2, "Dan":3}

for item in d:
    print(item)

for k in d:
#    print(k)
    print(d[k])

#Tuple unpacking!
mypairs = [(1,2),(3,4),(5,6)]

for (i,j) in mypairs:
    print(j)
    print(i)

# While loops
i =1

while i < 5:
    print("i is : {}".format(i))
    i = i+1


# Range functions
print(range(5))

print(list(range(0,5)))

# List Comprehension
x = [1,2,3,4]

out = []

for num in x:
    out.append(num**2)

print(out)

# Instead...

out = [num**2 for num in x]

print(out)
