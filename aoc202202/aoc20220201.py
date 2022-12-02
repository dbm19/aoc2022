#aoc202201

from pathlib import Path
import sys

def parse(puzzleInput):
  intermediatePuzzleInput = Path(puzzleInput).read_text().splitlines() 
  finalPuzzleInput = []

  for datum in intermediatePuzzleInput:
    datum = datum.split()
    finalPuzzleInput.append(datum)

  return finalPuzzleInput


def solve(puzzleInput):
  totalScore = 0

  for datum in puzzleInput:
    match datum[1]:
      case 'X': 
        totalScore += 1
        match datum[0]:
          case 'A':
            totalScore += 3
          case 'C':
            totalScore += 6
      case 'Y':
        totalScore += 2
        match datum[0]:
          case 'A':
            totalScore += 6
          case 'B':
            totalScore += 3
      case 'Z':
        totalScore += 3
        match datum [0]:
          case 'B':
            totalScore += 6
          case 'C':
            totalScore += 3
            
  return(totalScore)

if __name__ == "__main__":
  for path in sys.argv[1:]:
    print(solve(parse(path)))
