#
# Basic example of factory pattern
#

class Horse:

    """ A simple Horse class """

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Moo!"


class Rabbit:

    """ A simple Bird class """

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Squeak!"


def get_pet(pet="horse"):

    """ Basic Factory function """

    pets = dict(horse=Horse("Charlie"), rabgit=Rabbit("Coco"))

    return pets[pet]


# Getting horse object
horse = get_pet("horse")
print(horse.speak())

rabbit = get_pet("rabbit")
print(rabbit.speak())
