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
        match datum[0]:
          case 'A':
            totalScore += 3
          case 'B':
            totalScore += 1
          case 'C':
            totalScore += 2
      case 'Y':
        totalScore += 3
        match datum[0]:
          case 'A':
            totalScore += 1
          case 'B':
            totalScore += 2
          case 'C':
            totalScore += 3
      case 'Z':
        totalScore += 6
        match datum [0]:
          case 'A':
            totalScore += 2
          case 'B':
            totalScore += 3
          case 'C':
            totalScore += 1
            
  return(totalScore)

if __name__ == "__main__":
  for path in sys.argv[1:]:
    print(solve(parse(path)))
