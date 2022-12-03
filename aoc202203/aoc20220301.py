#aoc202201

from pathlib import Path
import sys

def parse(puzzleInput):
  puzzleInput = Path(puzzleInput).read_text().splitlines() 

  for i in range(len(puzzleInput)):
    firstCompartment, secondCompartment = puzzleInput[i][:len(puzzleInput[i])//2], puzzleInput[i][len(puzzleInput[i])//2:]
    puzzleInput[i] = [''.join(sorted(firstCompartment)), ''.join(sorted(secondCompartment))]

  return puzzleInput

def solve(puzzleInput):
  commonItem = ''
  commonItemPriority = 0
  sumOfPriorities = 0

  for i in range(len(puzzleInput)):
    j, k = 0, 0
    while j < len(puzzleInput[i][0]) and k < len(puzzleInput[i][1]):
      if puzzleInput[i][0][j] == puzzleInput[i][1][k]:
        commonItem = puzzleInput[i][0][j]
        if commonItem.isupper():
          commonItemPriority = ord(commonItem) - 38
        else:
          commonItemPriority = ord(commonItem) - 96
        sumOfPriorities += commonItemPriority
        break
      elif puzzleInput[i][0][j] < puzzleInput[i][1][k]:
        j += 1
      else:
        k += 1

  print(sumOfPriorities)

if __name__ == "__main__":
  for path in sys.argv[1:]:
    puzzleInput = parse(path)
    solve(puzzleInput)
