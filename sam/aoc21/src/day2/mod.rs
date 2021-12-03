use std::fs::File;
use std::io::{self, BufRead, Error};
use std::ops::Add;

const INPUT_FILE: &str = "./src/day2/input.txt";

#[derive(Debug)]
enum Command {
    Forward(i32),
    Backward(i32),
    Up(i32),
    Down(i32),
}

// I originally tried to used Serde, but it didn't work well, so I'm going for this instead.
impl Command {
    pub fn from_str(line: String) -> Command {
        let parts: Vec<&str> = line.split_ascii_whitespace().collect();
        let val = parts[1].parse::<i32>().unwrap();
        match parts[0] {
            "forward" => Self::Forward(val),
            "backward" => Self::Backward(val),
            "up" => Self::Up(val),
            "down" => Self::Down(val),
            _ => panic!("Unexpected command"),
        }
    }
}

#[derive(Default, Clone, Debug)]
struct Position {
    position: i32,
    depth: i32,
}

impl Position {
    fn empty() -> Self {
        Self {
            ..Default::default()
        }
    }

    /// Multiplies the final position by the final depth.
    fn output(&self) -> i32 {
        self.position * self.depth
    }
}

// By implementing this, we can calculate the final position just by summing the
// vec of commands.
impl Add<&Command> for Position {
    type Output = Position;

    fn add(self, rhs: &Command) -> Self::Output {
        let mut ret = self.clone();
        match &rhs {
            Command::Forward(val) => ret.position += val,
            Command::Backward(val) => ret.position -= val,
            Command::Up(val) => ret.depth -= val,
            Command::Down(val) => {
                ret.depth += val;
            }
        }
        ret
    }
}

#[test]
fn day2_task1() -> Result<(), Error> {
    let file = File::open(INPUT_FILE)?;
    let commands: Vec<Command> = io::BufReader::new(file)
        .lines()
        .map(|str| Command::from_str(str.unwrap()))
        .collect();
    let output: Position = commands.iter().fold(Position::empty(), |a, b| a + b);
    println!("Output for Task 1: {}", output.output());

    Ok(())
}

#[derive(Default, Clone, Debug)]
struct Position2 {
    position: i32,
    depth: i32,
    aim: i32,
}

impl Position2 {
    fn empty() -> Self {
        Self {
            ..Default::default()
        }
    }

    /// Multiplies the final position by the final depth.
    fn output(&self) -> i32 {
        self.position * self.depth
    }
}

impl Add<&Command> for Position2 {
    type Output = Position2;

    fn add(self, rhs: &Command) -> Self::Output {
        let mut ret = self.clone();
        match &rhs {
            Command::Forward(val) => {
                ret.position += val;
                ret.depth += ret.aim * val
            }
            Command::Backward(val) => {
                ret.position += val;
                ret.depth -= ret.aim * val
            }
            Command::Up(val) => ret.aim -= val,
            Command::Down(val) => ret.aim += val,
        }
        ret
    }
}

#[test]
fn day2_task2() -> Result<(), Error> {
    let file = File::open(INPUT_FILE)?;
    let commands: Vec<Command> = io::BufReader::new(file)
        .lines()
        .map(|str| Command::from_str(str.unwrap()))
        .collect();
    let output: Position2 = commands.iter().fold(Position2::empty(), |a, b| a + b);
    println!("Output for Task 2: {}", output.output());

    Ok(())
}
