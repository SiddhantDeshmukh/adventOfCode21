use std::fs::File;
use std::io::{self, BufRead, Error};

const INPUT_FILE: &str = "./src/day1/input.txt";

#[test]
fn day1_part1() -> Result<(), Error> {
    // First, get the puzzle input into an array.
    let file = File::open(INPUT_FILE)?;
    // Read each line of the file into a buffer and parse into an i32.
    let values: Vec<i32> = io::BufReader::new(file)
        .lines()
        .map(|val| val.unwrap().parse::<i32>().unwrap())
        .collect();
    // Now compare each of the vlaues in turn to see if the current is larger than the previous.
    let n_increase: i32 = (1..values.iter().count())
        .map(|i| if values[i] > values[i - 1] { 1 } else { 0 })
        .sum();

    println!("{} values increased.", n_increase);
    Ok(())
}

#[test]
fn day1_part2() -> Result<(), Error> {
    // First, get the puzzle input into an array.
    let file = File::open(INPUT_FILE)?;
    // Read each line of the file into a buffer and parse into an i32.
    let values: Vec<i32> = io::BufReader::new(file)
        .lines()
        .map(|val| val.unwrap().parse::<i32>().unwrap())
        .collect();
    // Now, construct our 3-wide window and iterate through the array of values.
    let n_increase: i32 = (3..values.iter().count())
        .map(|i| {
            if values[i - 2..i + 1].iter().sum::<i32>() > values[i - 3..i].iter().sum::<i32>() {
                1
            } else {
                0
            }
        })
        .sum();

    println!("{} 3-wide windows increased.", n_increase);
    Ok(())
}
