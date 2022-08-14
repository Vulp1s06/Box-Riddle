"""
This is a simulation of a riddle that I saw from Veritasium yt channel.

Riddle goes like this:
The director of a prison offers 100 death row prisoners, who are numbered from 1 to 100,
a last chance. A room contains a cupboard with 100 boxes.
The director randomly puts one prisoner's number in each closed box. The prisoners enter the room, one after another.
Each prisoner may open and look into 50 boxes in any order. The boxes are closed again afterwards.
If, during this search, every prisoner finds their number in one of the boxes, all prisoners are pardoned.
If just one prisoner does not find their number, all prisoners die.
Before the first prisoner enters the room, the prisoners may discuss strategy — but may not communicate once the first
prisoner enters to look in the boxes. What is the prisoners' best strategy?

If prisoners open the drawers randomly, their chance of success is 7.888609052×10^-31 which is insanely small.
But with the right metod the chance goes up to 0.31 or %31.

And the solution is:
Each prisoner first opens the drawer labeled with their own number.
If this drawer contains their number, they are done and were successful.
Otherwise, the drawer contains the number of another prisoner, and they next open the drawer labeled with this number.
The prisoner repeats steps 2 and 3 until they find their own number, or fail because the number is not found in the
first fifty opened drawers.
"""


import random


class Prisoner:
    def __init__(self, num, tries, successed=0):
        self.num = num
        self.tries = tries
        self.successed = successed

    def open_boxes(self, boxdict, successed=0):
        openedbox = boxdict[self.num]
        self.tries -= 1
        while self.tries > 0 and openedbox != self.num:
            openedbox = boxdict[openedbox]
            self.tries -= 1
        if openedbox == self.num:
            self.successed += 1
        else:
            pass

    def open_boxes_random(self, boxdict, successed=0):
        openedbox = boxdict[random.randint(1, 100)]
        self.tries -= 1
        while self.tries > 0 and openedbox != self.num:
            openedbox = boxdict[random.randint(1, 100)]
            self.tries -= 1
        if openedbox == self.num:
            self.successed += 1
        else:
            pass


successed_attempts_solution = 0
successed_attempts_random = 0
tries = 0

for i in range(10000):
    boxes = list(range(1, 101))
    inside_boxes = list(range(1, 101))
    random.shuffle(inside_boxes)
    mydict = {}
    counter = 0
    survived_prisoner_solution = 0
    survived_prisoner_random = 0
    for box_num in boxes:
        mydict[box_num] = inside_boxes[counter]
        counter += 1

    objs = [Prisoner(i, 50) for i in range(1, 51)]

    for obj in objs:
        obj.open_boxes(mydict)
        if obj.successed == 1:
            survived_prisoner_solution += 1

    for obj in objs:
        obj.open_boxes_random(mydict)
        if obj.successed == 1:
            survived_prisoner_random += 1

    if survived_prisoner_solution == 50:
        successed_attempts_solution += 1

    if survived_prisoner_random == 50:
        successed_attempts_random += 1
    tries += 1

print(
    f"Success rate with solution: in {tries} tries: %"
    + str(successed_attempts_solution / tries * 100)
)
print(
    f"Success rate with random: in {tries} tries: %"
    + str(successed_attempts_random / tries * 100)
)
