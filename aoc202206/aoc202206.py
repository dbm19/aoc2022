from pathlib import Path
import sys

def parse(inputFile):
  puzzleInput = Path(inputFile).read_text()
  return puzzleInput

def solve(puzzleInput, length):
  for i in range(0, len(puzzleInput)):
    array = puzzleInput[i:i+length]
    isMarker = True

    for j, c in enumerate(array):
      if array.count(c) != 1:
        isMarker = False
        break
      if isMarker == True and j == length-1:
        sopMarkerIndex = i
        print(i+length)
        return(i)

if __name__ == '__main__':
  for path in sys.argv[1:]:
    puzzleInput = parse(path)
    solve(puzzleInput, 4)
    solve(puzzleInput, 14)
