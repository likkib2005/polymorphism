class Duck:
    def swim(self):
        print("I am a duck and I can swim")
    def speaks(self):
        print("I am a duck and I can speak")
class Dog:
    def swim(self):
        print("I am a dog and I can swim")
    def speaks(self):
        print("I am dog and I can speak")
class Person:
    def speak(self):
        print("I am a person and I can speak")
def display(duck):
    duck.swim()
    duck.speaks()
    print("Information displayed")
duck=Duck()
dog=Dog()
p=Person()
display(duck)
display(dog)
display(p)