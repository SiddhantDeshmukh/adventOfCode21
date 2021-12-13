# https://adventofcode.com/2021/day/8
using AdventOfCode

input = readlines("./data/day_08.txt")

# Dictionary containing signal values for each digit
segments = Dict(
  0 => ['a', 'b', 'c', 'e', 'f', 'g'],
  1 => ['c', 'f'],  # only 2
  2 => ['a', 'c', 'd', 'e', 'g'],
  3 => ['a', 'c', 'd', 'f', 'g'],
  4 => ['b', 'c', 'd', 'f'],  # only 4
  5 => ['a', 'b', 'd', 'f', 'g'],
  6 => ['a', 'b', 'd', 'e', 'f', 'g'],
  7 => ['a', 'c', 'f'],  # only 3
  8 => ['a', 'b', 'c', 'd', 'e', 'f', 'g'],  # only 7
  9 => ['a', 'b', 'c', 'd', 'f', 'g'],
)


function read_signals_values(input)
  signals, values = [], []
  for line in eachrow(input)
    split_line = split(line[1], " | ")
    push!(signals, split_line[1])
    push!(values, split_line[2])
  end
  return signals, values
end


function part_1(input)
  signals, values = read_signals_values(input)
  count = 0
  for line in eachrow(values)
    nums = split(line[1], " ")
    for n in nums
      if length(n) in [2, 3, 4, 7]
        count += 1
      end
    end
  end

  return count
end
@info part_1(input)

function part_2(input)
  nothing
end
@info part_2(input)

