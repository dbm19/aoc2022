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
  array = []
  sumOfTopThree = 0

  for datum in puzzle_input:
    if datum != '':
      elfCalories += datum
    else:
      array.append(elfCalories)
      elfCalories = 0

  array.sort()  
  
  for i in range(len(array) - 3, len(array)):
    sumOfTopThree += array[i]  

  print(array, sumOfTopThree, len(array))

if __name__ == "__main__":
  for path in sys.argv[1:]:
    puzzle_input = parse(Path(path).read_text().splitlines())
    solve(puzzle_input)
