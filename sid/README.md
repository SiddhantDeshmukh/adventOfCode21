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
