#aoc202201

from pathlib import Path
import sys

def parse(inputFile):
  puzzleInput = [x.split(',') for x in Path(inputFile).read_text().splitlines()]
  for i in range(len(puzzleInput)):
    puzzleInput[i][0] = puzzleInput[i][0].partition('-')    
    puzzleInput[i][1] = puzzleInput[i][1].partition('-')
  return puzzleInput

def solvePartOne(puzzleInput):
  totalPairsOverlapping = 0

  for i in range(len(puzzleInput)):
    print(i + 1, totalPairsOverlapping)
    if compareOne(puzzleInput[i][0], puzzleInput[i][1]):
      totalPairsOverlapping += 1
      continue
    elif compareOne(puzzleInput[i][1], puzzleInput[i][0]):
      totalPairsOverlapping += 1
      continue
    else:
      continue
  print(totalPairsOverlapping)   

def solvePartTwo(puzzleInput):
  totalPairsOverlapping = 0

  for i in range(len(puzzleInput)):
    print(i + 1, totalPairsOverlapping)
    if compareTwo(puzzleInput[i][0], puzzleInput[i][1]):
      totalPairsOverlapping += 1
      continue
    elif compareTwo(puzzleInput[i][1], puzzleInput[i][0]):
      totalPairsOverlapping += 1
      continue
    else:
      continue
  print(totalPairsOverlapping)

def compareOne(sections1, sections2):
  if int(sections1[0]) >= int(sections2[0]) and int(sections1[2]) <= int(sections2[2]):
      return True
  else:
      return False

def compareTwo(sections1, sections2):
  if int(sections1[0]) >= int(sections2[0]) and int(sections1[2]) <= int(sections2[2]):
    return True
  elif int(sections1[2]) >= int(sections2[0]) and int(sections1[0])  <= int(sections2[0]):
    return True 
  elif int(sections1[0]) <= int(sections2[2]) and int(sections1[2]) >= int(sections2[2]):
    return True
  else:
    return False

if __name__ == "__main__":
  for path in sys.argv[1:]:
    puzzleInput = parse(path)
    solvePartOne(puzzleInput)
    solvePartTwo(puzzleInput)
