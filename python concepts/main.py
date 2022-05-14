class Animal:
    friends =[]

    def __init__(self,height=100,weight=50):
        self.height =height
        self.weight =weight
        self._private_weight = 70 # Private variable
        self.__very_private = 10

    def print_height(self):
        print(f"this animal's height is {self.get_height()}")

    def get_height(self):
        return self.height

    def get_fur_color(self):
        return self.fur_color

    def get_friends(self):
        return self.friends

    def set_height(self,height):
        self.height = height

    def greet(self):
        print("this animal makes no sound")

# animal1 = Animal(200,40)
# animal1.print_height()
# animal2 = Animal(400,70)
# animal3 = Animal()
# print(animal2.get_height())
# print(animal2.height)
#
# print(animal1.fur_color)
# print(animal2.fur_color)
#
# animal2.fur_color = "pink"
#
# animal1.friends.append("jerry")
# print(animal1.friends, animal2.friends)
#
# print(animal3.height)
# animal3.set_height(90)
# print(animal3.height)
#
# print(animal3._private_weight)

class Dog(Animal):
    def __init__(self,height,weight,fur_color):
        self.fur_color = fur_color
        super().__init__(height=height,weight=weight)

    @classmethod
    def greet(self):
        print(f"woof woof")



sample_dog = Dog(50,25,"brown")
print(sample_dog.fur_color, sample_dog.height,sample_dog.weight)
sample_dog.print_height()
sample_dog.greet()

Dog.greet()
print(" A dog's starting friends are: ", Dog.friends)