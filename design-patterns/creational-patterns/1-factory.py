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

