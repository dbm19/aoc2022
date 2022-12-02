#aoc20150101

import pathlib
import sys

def parse(puzzleInput):
  return list(pathlib.Path(puzzleInput).read_text().splitlines())

def solve(puzzleInput):
  totalLength = 0

  for datum in puzzleInput:
    formattedDatum = datum.split('x')
    wrapLengthArray = []
    ribbonLength = 0
    wrapLength = 0

    ribbonLength = int(formattedDatum[0]) * int(formattedDatum[1]) * int(formattedDatum[2])

    wrapLengthArray.append(int(formattedDatum[0]))
    wrapLengthArray.append(int(formattedDatum[1]))
    wrapLengthArray.append(int(formattedDatum[2]))
    wrapLengthArray.sort()

    wrapLength = (2 * wrapLengthArray[0]) + (2 * wrapLengthArray[1])

    totalLength += ribbonLength + wrapLength

  print(totalLength)

if __name__ == "__main__":
  for path in sys.argv[1:]:
    solve(parse(path))
