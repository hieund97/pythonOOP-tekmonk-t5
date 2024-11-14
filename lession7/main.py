class Animal():

    def __init__(self, type):
        self.type = type

    def breath(self):
        print("I can breath")

    def skill(self):
        print("I run fast like the light")
        
    def hibernate(self):
        print("Animal can be hibernated in winter")


class Snake(Animal):

    def __init__(self, type, name):
        super().__init__(type)
        self.name = name

    def breath(self):
        print("I can breath under water")


class Cat(Animal):

    def __init__(self, type, name, food_type):
        super().__init__(type)
        self.name = name
        self.food_type = food_type

    def skill(self):
        print("I can catch the mice")


class Tiger(Animal):

    def __init__(self, type, name, sleep):
        super().__init__(type)
        self.name = name
        self.sleep = sleep

    def hibernate(self):
        print("Tiger is hibernated")
        
ansible, cairo, fluid-synth, glib, google-cloud-sdk, harfbuzz, python-tk@3.12, sdl2_mixer and sdl2_ttf


snake = Snake("poision", "tiger")

snake2= Snake("non-poision", "tiger")

bamboo = Animal("non-poision")
