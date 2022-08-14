import random


class Prisoner:
    def __init__(self, num, tries, successed=0):
        self.num = num
        self.tries = tries
        self.successed = successed

    def open_boxes(self, boxdict):
        openedbox = boxdict[self.num]
        self.tries -= 1
        while self.tries > 0 and openedbox != self.num:
            openedbox = boxdict[openedbox]
            self.tries -= 1
        if openedbox == self.num:
            self.successed += 1
        else:
            pass

    def open_boxes_random(self, boxdict):
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
