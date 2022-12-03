#aoc202201

from pathlib import Path
import sys

def parse(puzzleInput):
  puzzleInput = Path(puzzleInput).read_text().splitlines() 
  newPuzzleInput = []

  for i in range(0, len(puzzleInput), 3):
    newPuzzleInputDatum = []
    for j in range(3):
      newPuzzleInputDatum.append(''.join(sorted(puzzleInput[i + j])))
    newPuzzleInput.append(newPuzzleInputDatum)
  
  return newPuzzleInput

def solve(puzzleInput):
  commonItem = ''
  commonItemPriority = 0
  sumOfPriorities = 0

  for i in range(len(puzzleInput)):
    j, k = 0, 0
    commonItemArray = []
    while j < len(puzzleInput[i][0]) and k < len(puzzleInput[i][1]):
      if puzzleInput[i][0][j] == puzzleInput[i][1][k]:
        commonItem = puzzleInput[i][0][j]
        commonItemArray.append(commonItem)
        j += 1
        k += 1
      elif puzzleInput[i][0][j] < puzzleInput[i][1][k]:
        j += 1
      else:
        k += 1
    l, m = 0, 0
    while l < len(commonItemArray) and m < len(puzzleInput[i][2]):
      if commonItemArray[l] == puzzleInput[i][2][m]:
        commonItem = commonItemArray[l]
        if commonItem.isupper():
         commonItemPriority = ord(commonItem) - 38
        else:
          commonItemPriority = ord(commonItem) - 96
        sumOfPriorities += commonItemPriority
        break
      elif commonItemArray[l] < puzzleInput[i][2][m]:
        l += 1
      else:
        m += 1
    print(puzzleInput[i], commonItemArray, commonItem)
  print(sumOfPriorities)

if __name__ == "__main__":
  for path in sys.argv[1:]:
    puzzleInput = parse(path)
    solve(puzzleInput)
