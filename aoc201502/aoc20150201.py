#aoc20150101

import pathlib
import sys

def parse(puzzleInput):
  return list(pathlib.Path(puzzleInput).read_text().splitlines())

def solve(puzzleInput):
  totalArea = 0

  for datum in puzzleInput:
    formattedDatum = datum.split('x')
    areas = []

    areaOne = int(formattedDatum[0]) * int(formattedDatum[1])
    areaTwo = int(formattedDatum[0]) * int(formattedDatum[2])
    areaThree = int(formattedDatum[1]) * int(formattedDatum[2])

    areas.append(areaOne)
    areas.append(areaTwo)
    areas.append(areaThree)
    areas.sort()

    presentArea = (2 * areaOne) + (2 * areaTwo) + (2 * areaThree) + areas[0]
    totalArea += presentArea

  print(totalArea)

if __name__ == "__main__":
  for path in sys.argv[1:]:
    solve(parse(path))
