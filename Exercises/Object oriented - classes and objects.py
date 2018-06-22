class pound:

    value = 1.00
    color = "gold"
    num_edges = 1
    diameter = 22.5 #mm
    thickness = 3.15 #mm
    heads = True


coin1 = pound()

print coin1.value
print coin1.color

coin1.color = "Green"

coin2 = pound()

print coin2.color
print coin1.color


coin1.value = 2.5

print coin1.value
print coin2.value

#______________________________________________________________________________
import random

class Coin:
    def __init__(self,rare=False, clean=True, heads=True, **kwargs):

        for key,values in kwargs.items():
            setattr(self,key,values)


        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value  * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

    def rust(self):
        self.color = self.rusty_color

    def clean(self):
        self.color = self.clean_color

    def __del__(self):
        print "Coin spent !"

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads=choice


class pound(Coin):
    def __init__(self):
        data = {
            "original_value": 1.00,
            "clean_color": "gold",
            "rusty_color": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
        }

    super().__init__(**data)



