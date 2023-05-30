class Animal:
    def eat(self):
        print("Eating... in animal class")


class Mammal(Animal):
    def sleep(self):
        print("Permitted to sleep")


class Fish(Animal):
    def swim(self):
        print("i can swim")


f = Fish()
print(f.eat())

