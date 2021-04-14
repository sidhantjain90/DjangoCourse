class Dog():

    #Class Object Attribute
    species = "mammal"

    def __init__(self,breed, name):
        self.breed = breed
        self.name = name


mydog = Dog("Lab","Tom")

print(mydog.breed)
print(mydog.name)
print(mydog.species)


class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius*self.radius*Circle.pi

    def setRadius(self,new_r):
        self.radius = new_r

myc = Circle(3)
myc.setRadius(999)
print(myc.area())



#Inheritance

class Animal():

    def __init__(self):
        print('Animal Created')

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print('Eating')


class Dog1(Animal):

    def __init__(self):
        #Animal.__init__(self)
        print("Dog Created")

    def bark(self):
        print("Woof")

    def eat(self):
        print("Dog Eating")

mya = Animal()
mya.whoAmI()
mya.eat()

myd = Dog1()
myd.whoAmI()
myd.eat()
myd.bark()


#Special Methods

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

b = Book("Python","jose",200)
print(len(b))
