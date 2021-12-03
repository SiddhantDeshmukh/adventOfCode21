use std::fs::File;
use std::io::{self, BufRead, Error};

/// Reads lines from a file as text and returns them as a vec (wrapped in a result).
pub fn read_lines(filename: String) -> Result<Vec<String>, Error> {
    // First, get the puzzle input into an array.
    let file = File::open(filename)?;
    // Read each line of the file into a buffer and return.
    let values: Vec<String> = io::BufReader::new(file)
        .lines()
        .map(|line| line.unwrap())
        .collect();
    Ok(values)
}
