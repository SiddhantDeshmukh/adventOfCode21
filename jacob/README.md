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