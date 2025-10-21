class Coffee:
    def __init__(self, type, strength):
        self.type = type
        self.strength = strength
    
class HotCoffee(Coffee):
    def __init__(self, type, strength, flavour):
        self.type = type
        self.strength = strength
        self.flavour = flavour

class WarmCoffee(Coffee):
    def __init__(self, type, strength, flavour):
        Coffee.__init__(self, type, strength)
        self.flavour = flavour

class ColdCoffee(Coffee):
    def __init__(self, type, strength, flavour):
        super().__init__(type, strength)
        self.flavour = flavour


