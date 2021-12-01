# Advent of Code 2021 - Sam's Rusty Funhouse

Here are my implementation of the Advent of Code 2021 problems using Rust. I have decided to run said tests using Rust's build in testing framework. I have structured the crate such that each day has its own self-contained module. As a result of this, all of the tests for AOC2021 can be run using

```bash
cargo test --all-features
```

To run only those tests that pertain to a given day, use

```bash
cargo test day<n> --all-features [-- --nocapture]
```

For example running the tasks for day 1 would be `cargo test day1 --all-features`. You can optionally include what is in the brackets to see the output from the tests. 

## Advent Calendar (of Code)

- [x] Day 1
- [ ] Day 2
- [ ] Day 3
- [ ] Day 4
- [ ] Day 5
- [ ] Day 6
- [ ] Day 7
- [ ] Day 8 
- [ ] Day 9
- [ ] Day 10
- [ ] Day 11
- [ ] Day 12
- [ ] Day 13
- [ ] Day 14
- [ ] Day 15
- [ ] Day 16
- [ ] Day 17
- [ ] Day 18
- [ ] Day 19
- [ ] Day 20
- [ ] Day 21
- [ ] Day 22
- [ ] Day 23
- [ ] Day 24