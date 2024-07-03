print("sample")
our_list = [2, 4, 8]
var = 4
word = 'good'
print()
print(type(our_list))
print(type(var))
print(type(word))
print(type({}))
our_list = our_list.append("new")
our_list
print()
# class Car:
#     def __init__(self, color, make, model):
#         self.color = color
#         self.b = make
#         self.c = model
#         # print("new instance of car created")
#     def describe(self):
#         print(f"this is a {self.color} {self.make} {self.model}")


# car1 = Car("blue", "toyota", "camry")
# car2 = Car("accord", "honda", "accord")
# vehicle3 = Car("grey", "lexus", "jeep")


# car1.describe()
# vehicle3.describe()










class Animals:
    def __init__(self, age, height, weight, colour):
        self.cm = height
        self.kg = weight
        self.race = colour
        self.num = age
def describe(self):
    print(f'this is a {self.num}yrs old {self.race} {self.kg} animal, with a height of {self.cm}')    

class Mammal(Animals):

    def describe(self):
        print(f'this is a {self.num}yrs old {self.race} {self.kg} animal, with a height of {self.cm}')

        
cat1 = Mammal(2, "2.4cm", "6kg", "white")
cat1.describe()
cat1.describeMammal()


cat1 = Animals(6, "9.4cm", "3kg", "white")
cat1.describe()
cat1.describeMammal()


Anim1.describe()
print(Anim1.kg)
Anim1.kg = '6kg'
Anim1.describe()




