use crate::common;
use std::collections::HashMap;
use std::error::Error;
use std::result::Result;

const INPUT_FILE_NAME: &str = "./src/day3/input.txt";

#[test]
pub fn day3_task1() -> Result<(), Box<dyn Error>> {
    // Read the lines in from the input file.
    let lines = common::read_lines(INPUT_FILE_NAME.into())?;
    let width = lines[0].chars().count();
    println!("{}", width);

    // First, find the most common bits in the input report.
    let most_common: String = (0..width)
        .into_iter()
        .map(|ibit| {
            let bits = lines
                .iter()
                .map(|str| str.chars().nth(ibit).unwrap())
                .collect::<Vec<char>>();

            let mut occurrences = HashMap::new();

            // This part was inspired by this method of finding the mode.
            // https://codereview.stackexchange.com/questions/173338/calculate-mean-median-and-mode-in-rust
            for value in bits {
                *occurrences.entry(value).or_insert(0) += 1;
            }

            occurrences
                .into_iter()
                .max_by_key(|&(_, count)| count)
                .map(|(val, _)| val)
                .unwrap()
        })
        .collect();

    // As this is a binary choice, just bitflip the least common.
    let least_common: String = most_common
        .chars()
        .map(|char| if char == '1' { '0' } else { '1' })
        .collect();

    let gamma_rate = i32::from_str_radix(&most_common, 2).unwrap();
    let epsilon_rate = i32::from_str_radix(&least_common, 2).unwrap();
    println!("{} {}", gamma_rate, epsilon_rate);
    let power_consumption = epsilon_rate * gamma_rate;
    println!("The power consumption for task 1 is {}", power_consumption);

    Ok(())
}

#[test]
pub fn day3_task2() -> Result<(), Box<dyn Error>> {
    // Read the lines in from the input file.
    let lines = common::read_lines(INPUT_FILE_NAME.into())?;
    let width = lines[0].chars().count();
    println!("{}", width);

    // First, find the most common bits in the input report.
    let most_common: String = (0..width)
        .into_iter()
        .map(|ibit| {
            let bits = lines
                .iter()
                .map(|str| str.chars().nth(ibit).unwrap())
                .collect::<Vec<char>>();

            let mut occurrences = HashMap::new();

            // This part was inspired by this method of finding the mode.
            // https://codereview.stackexchange.com/questions/173338/calculate-mean-median-and-mode-in-rust
            for value in bits {
                *occurrences.entry(value).or_insert(0) += 1;
            }

            // This whole thing is to make sure that we favour one if both are equal. 
            let mut occ_vec = occurrences.into_iter().collect::<Vec<(char, i32)>>();
            occ_vec.sort_by(|&(vala, _), &(valb, _)| vala.cmp(&valb));
            occ_vec.into_iter()
                .max_by_key(|&(_, count)| count)
                .map(|(val, _)| val)
                .unwrap()
        })
        .collect();
    
    // As this is a binary choice, just bitflip the least common.
    let least_common: String = most_common
        .chars()
        .map(|char| if char == '1' { '0' } else { '1' })
        .collect();

    // So we need the most common bits, however we need to rework everything past this point.
    let mut o2_lines = lines.clone();
    let mut co2_lines = lines.clone();
    for ibit in 0..width {

        if o2_lines.iter().count() > 1 {
            o2_lines = o2_lines
                .into_iter()
                .filter(|val| val.chars().nth(ibit) == most_common.chars().nth(ibit))
                .collect();
        }
        if co2_lines.iter().count() > 1 {
            co2_lines = co2_lines
                .into_iter()
                .filter(|val| val.chars().nth(ibit) == least_common.chars().nth(ibit))
                .collect();
        }

        println!("{:?}", co2_lines);
    }

    let o2_generator_rating = u32::from_str_radix(o2_lines.first().unwrap(), 2).unwrap();
    let co2_scrubber_rating = u32::from_str_radix(co2_lines.first().unwrap(), 2).unwrap();
    let output = o2_generator_rating * co2_scrubber_rating;
    println!("Life support rating from task 2: {}", output);
    // NOTE: This is not yet working. I will come back to it later. 
    // If you were curious, this looks like a nice solution to this:
    // https://github.com/ephemient/aoc2021/blob/main/rs/src/day3.rs

    Ok(())
}
