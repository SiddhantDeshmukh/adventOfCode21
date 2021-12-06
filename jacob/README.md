# How to Run
The package should be first built with 'cargo build' or 'cargo run' and then the executable can be run independently. 

# My Attempts with Comments

I think it's most efficient to make one cargo project with one main file, and then run each day (from another imported .rs file) from there. 

## Day 0
Set up calling functions from other files. Using a "match" expression for flexibility.

## Day 1
Calculating relative depths. First for adjacent measurements and then for a sliding window 3 measurements wide. Used Vectors and a for-loop, so I'm sure it could be more efficient. 

## Day 2
Calculate the changing position of our submarine. The commands come in form ("command", value) and needed to be parsed. Pretty straightforward use of a match expression once I split the commands and position into structs.

## Day 3
Needed to calculate the most and least common bit values in series of bit arrays. For part 1 it was easy to take the sum of an array of "bytes" along each column, and then check whether the sum was > len(array)/2, if so set the value to 1 for gamma, 0 otherwise. Epsilon was always !gamma. In part 2, the summation had to be redone for each set of "valid" bit arrays, but otherwise same logic. I could probably have made it more efficient in part 2 only taking sum of an individual column rather than all bits, but addition is cheap...

## Day 4
Bingo! How hard could it be... I stored each "board" as a hashmap (like python dict) for fast lookup of whether a number was in a board. This worked well for part 1, finding the first winning board. Part 2 is finding the last, and for whatever reason it works on the test data but not the real input yet.

## Day 5
Given line start/end coordinates, find where they cross. I made Line and Map structs to hold the data, and saved the coordinates along each line. I found out that you can't make an array [usize;1000000] but you can make a vector equally long, due to stack overflow. Part 1 was just horiz/vert lines, and part 2 added diagonal. All the magic happens in the file processing function which formats the lines nicely.

## Day 6
Exponential fish spawning! In part 1 I simply made a Fish struct and iterated overall fish on a given day, making more fish when timers ran out. This of course becomes crazy for a large number of days, and part 2 punished me for taking the easy way out. In part 2 I have an array with N_fish on each day, and then I spawn fish in batches and "school" the fish at the end of a cycle to account for new spawns. Should scale linearly with N_days. 