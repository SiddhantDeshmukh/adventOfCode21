# Generates boilerplate for given day
import sys
import pathlib

day = sys.argv[1]
ROOT = pathlib.Path(__file__).parent.absolute()
src = f'{ROOT}/src'
data = f'{src}/data'
base_url = f"https://adventofcode.com/2021/day/{day}"


boilerplate = f"""# {base_url}
using AdventOfCode

input = readlines("./data/day_{day.zfill(2)}.txt")

function part_1(input)
  nothing
end
@info part_1(input)

function part_2(input)
  nothing
end
@info part_2(input)

"""

out_path = f'{src}/day_{day.zfill(2)}.jl'

if pathlib.Path.is_file(out_path):
  print("Error: File exists!")
else:
  with open(out_path, 'w', encoding='utf-8') as outfile:
    outfile.write(boilerplate)
