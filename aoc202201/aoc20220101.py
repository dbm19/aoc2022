#aoc202201

from pathlib import Path
import sys

def parse(puzzle_input):
  array = []

  for datum in puzzle_input:
    if datum != '':
      array.append(int(datum))
    else:
      array.append(datum)
  return array

def solve(puzzle_input):
  elfCalories = 0
  largestElfCalories = 0

  for datum in puzzle_input:
    if datum != '':
      elfCalories += datum
    else:
      if elfCalories > largestElfCalories:
        largestElfCalories = elfCalories
      elfCalories = 0

  print(largestElfCalories)  


if __name__ == "__main__":
  for path in sys.argv[1:]:
    print(f"{path}:")
    puzzle_input = parse(Path(path).read_text().splitlines())
    print(puzzle_input)
    solve(puzzle_input)
