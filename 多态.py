class Animal(object):
    def __init__(self,name):
        self.name = name
    def talk(self):
        raise NotADirectoryError('Subclass must implement abstract menthod')
    @staticmethod
    def animal_talk(obj):
        obj.talk()

class Cat(Animal):
    def talk(self):
        print('Meow!')

class Dog(Animal):
    def talk(self):
        print('Woof! Woof!')



d = Dog('chengronghua')
# d.talk()

c = Cat('xuliangwei')
# c.talk()

Animal.animal_talk(c)
Animal.animal_talk(d)
