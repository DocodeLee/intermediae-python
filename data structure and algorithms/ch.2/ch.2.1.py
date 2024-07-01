import random

class MSDie:
    """Multi sided die
    Instance Variables:
        current value
        num slides
    """
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()
    
    def roll(self):
        self.current_value = random.randrange(1, self.num_sides +1)
        return self.current_value
    
    def __str__(self):
        return str(self.current_value)
    def __repr__(self):
        return "MSDie({}) : {}".format(self.num_sides, self.current_value)

my_dice = MSDie(6)
for i in range(5):
    print(my_dice, my_dice.current_value)
    my_dice.roll()

d_list = [MSDie(6), MSDie(20)]
print(d_list)