# Star-Traversal

A greedy algorithm was applied to calculate the path between the stars and provide the total distance to travel based on the HYG (Hipparcos, Yale, Gliese) database (v2.0)

In order to create a feasible star traversal path, we start at the Sol (our sun), then jump to the nearest star (that is within our specified radius of the Sol). By continuing to the next nearest star that hasn’t been visited, we visit all the stars that are within our specified radius of the Sol.

In this work, 10 parsecs is selected as the radius of the Sol for the star traversal. A for loop is applied to calculate the distance between all the stars and the Sol in the HYG database to filter out stars that are outside of 10 parsecs radius of the Sol. The rest stars are counted and introduced into hash tables (in python, a dictionary data structure works as a hash table), which contain star IDs, star names and the x, y, and z rectangular coordinates.

A greedy algorithm is applied to calculate the nearest star that hasn’t been visited ( the minimization of the distance from the current star to the stars that haven’t been visited is the key to determine which is the next star that we will jump to). The current star name, the nearest star name, the star-star travel distance and the total travel distance will be printed out as the output. The star traversal path will be shown in a 3D plot.
