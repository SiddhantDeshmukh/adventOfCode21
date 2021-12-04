# Advent of Code 2021

In this directory are my solutions to the Advent of Code 2021 puzzles done
in Julia. And I'll write my thoughts about each day's challenges below!

## Day 1 - Sonar Sweep

Today was focused on finite differencing arrays based on different windows.
Part 1, quite simply, involved computing a finite difference of the input
and counting the number of positive elements. Julia helpfully provides a
'diff' function that just does this, so for me this was a breeze.

Part 2 was more complicated, using a 3-element sliding window and the sum
of the elements. Keeping the finite differencing idea in mind, I looped
over the input in 3-element windows, summing each one and adding it to
an array. At the end, I applied the same finite difference
positive-counting method on this new array whose elements were the window
sums. All in all, a good start!

## Day 2 - Dive!

I solved this using vectors, assigning coordinates [pos, depth] for part 1
and [pos, depth, aim] for part 2. The instructions for the submarine are
stored in a dictionary. In part 1, this dictionary contains the array that
should be multipled by the value 'X' to get the new [pos, depth]. In part 2,
the dictionary contains the 'forward', 'down', 'up' functions to directly
update the coordinates.

One way I could clean it up (but I won't since I want the solutions to be as-
attempted) is to package the loop over the 'input' into a function that updates
the coordinates at each step. Essentially, create an update function (rules)
for each part (Dict of functions) and then pass this Dict of instructions in as
well. The function should just return the final coords!

Update: I went ahead and did it in the 'learn' directory, which I'll use to
write improvements to the challenges!

## Day 3 - Binary Diagnostic

Part 1 waws pretty straightforward but I struggled to finish part 2 in Julia.
I spent a lot of time trying to come up with mathematical tricks to avoid
looping, but in the end just bit the bullet and wrote out the loops. Oh
well, would love to improve the code!

## Day 4 - Squid Bingo

Difficulty is picking up! I spent a long time trying to figure out how to create
a 3D array in Julia from the input provided, and eventually just resigned
myself to looping. Really hope there's a nicer way to turn an array of 2D arrays
into a 3D array (and higher order versions)! After figuring out the data, part 1
was a little finnicky because there were lots of small things I had to check
for. In the end, I added a 'scoreboard' for each bingo board that was
initialised with zeroes. For every 'hit', the corresponding scoreboard value
would become 1. This makes it easy to check for a bingo!

I really think my code is too long, but I can't find a nicer way to do it; a
quarter is just to load in the data! I suspect there is a much better way to
do for loops akin to 'itertools.product' (or at least to go over every index).
Part 2 wasn't much harder because of the way I'd written the code, I just had
to change the rules for the 'win' condition. Onto the next one!
