import random
import sys
import os

print("Hello World")

name = "Derek"
print(name)

#5 Main Datatypes Numbers, String, Tuples, Dictionary
#7 Different Arithmetic operators + - * / % ** //

#Numbers
print("5 + 2 =", 5+2)
print("5 - 2 =", 5-2)
print("5 * 2 =", 5*2)
print("5 / 2 =", 5/2)
print("5 % 2 =", 5%2)
print("5 ** 2 =", 5**2)
print("5 // 2 =", 5//2)

#String

quote = "\" Always remember you are unique"
multi_line_quote = ''' just
like everyone else '''

print("%s %s %s" %('I like the qoute',quote,multi_line_quote))

print("I don't like", end="")
print("newline")

#List

grocery_list = ['Juice','Tomatoes','Potatoes']

print('First item',grocery_list[0])

grocery_list[0] = "Green juice"
print("First item",grocery_list[0])

print(grocery_list[1:2])

other_events = ['Car','wash','bike']

to_do_list = (grocery_list,other_events)

print(to_do_list)
print(to_do_list[0][1])

grocery_list.insert(1,"Pickle")
grocery_list.remove("Pickle")
grocery_list.sort()
grocery_list.reverse()
del grocery_list[2]
print(to_do_list)

#Tuple
pi_tuple = (3,3,5,7,8)

new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)

len(new_tuple)

#Dictionary

super_villains = {'Fiddler': 'Isaac Bowin',
                  'Captain Cold' : 'Leonard Snart',
                  'Weather Wizard' : 'Mark Mardon',
                  'Mirror Master' : 'Sam Scuuder',
                  'Pied Piper' : 'Thomas Peterson'}

print(super_villains['Captain Cold'])
del super_villains['Fiddler']
super_villains['Pied Piper'] = 'Hartley Rathaway'
print(len(super_villains))
print(super_villains.get("Weather Wizard"))
print(super_villains.keys())
print(super_villains.values())

#Conditional

age = 30

if age > 16 :
    print('You are old enough to drive')
else:
    print("You are not old enough to drive")

if age >= 21 :
    print('You are old enough to drive a truck')
elif age >= 16 :
    print('You are old enough to drive a car')
else :
    print('You are not old enough to drive a car')

#Logical

if ((age >= 1 ) and (age <= 18)) :
    print("You get a birthday")
elif (age == 21) or (age >= 65) :
    print("You are getting a birthday")
elif not(age==30) :
    print("You don't get a birthday")
else:
    print("You get a birthday party yeah ")

#Loop

#forloop
for x in range(0,10):
    print(x,'',end="")

grocery_list = ['Juice', 'Tomatoes', 'Potatoes',
                'Bananas']
for y in grocery_list:
    print(y)

for x in [2,4,6,8,10]:
    print(x)

num_list = [[1,2,3],[10,20,30],[100,200,300]]
for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])

#while

random_num = random.randrange(0,100)

while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)

i = 0;
while(i <= 20):
    if(i%2 == 0):
        print(i)
    elif(i == 9):
        break
    else:
        i += 1
        continue

    i += 1

#function

def addNumber(fNum , lnum):
    sumNum = fNum + lnum
    return sumNum
print(addNumber(1 , 4))

print('what is your name')
name = sys.stdin.readline()
print('Hello', name)

#File IO

test_file = open("test.txt", "wb")
print(test_file.mode)
print(test_file.name)
test_file.write(bytes("Write me to the file\n", 'UTF-8'))
test_file.close()
test_file = open("test.txt", "r+")
text_in_file = test_file.read()
print(text_in_file)



#Objects

class Animal:
    __name = ""
    __height = ""
    __weight = 0
    __sound = 0

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound
#Add all getter and setter

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_type(self):
        print('Animal')

    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {}".format(self.__name,
                                                                     self.__height,
                                                                     self.__weight,
                                                                     self.__sound)

    cat = Animal('Whiskers',33, 10, 'Meow')
    print(cat.toString())

#inheritance

class Dog(Animal):
    __owner = ""
    
    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def __get__(self):
        return self.__owner
    def get_type(self):
        print("Dog")
    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {} His owner is {}".format(self.__name,
                                                                     self.__height,
                                                                     self.__weight,
                                                                     self.__sound,
                                                                    self.__owner)
    spot = Dog("Spot", 53, 27 , "Ruff", "Derek")
    print(spot.toString())

#Polymorphism

class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()
test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(spot)