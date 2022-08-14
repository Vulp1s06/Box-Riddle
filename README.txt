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
