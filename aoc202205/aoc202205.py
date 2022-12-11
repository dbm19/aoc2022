#aoc202201

from pathlib import Path
import sys

def parse(inputFile):
  puzzleInput = Path(inputFile).read_text().splitlines()

  for i in range(0, 8):
    array = []
    for j in range(0, len(puzzleInput[i]), 4):
      array.append(puzzleInput[i][j:j+3])
    puzzleInput[i] = array

  for i in range(10, len(puzzleInput)):
    array = []
    puzzleInput[i] = puzzleInput[i].split(" ")
    for j in puzzleInput[i]:
      if j.isdigit():
        array.append(j)
    puzzleInput[i] = array

  return puzzleInput

def solve(puzzleInput, type):
  stacks = {}

  for i in range(0, 8):
    for j in range(0, len(puzzleInput[i])):
      if puzzleInput[i][j] != "   ":
        if "{}".format(j+1) in stacks:
          stacks["{}".format(j+1)].insert(0, puzzleInput[i][j])
        else:
          stacks["{}".format(j+1)] = [puzzleInput[i][j]]

  for i in range(10, len(puzzleInput)):
    rearrangeStacks(type, int(puzzleInput[i][0]), stacks["{}".format(puzzleInput[i][1])], stacks["{}".format(puzzleInput[i][2])])
  print(stacks)


def rearrangeStacks(type, amt, stack1, stack2):
  if type == 1:
    for i in range(amt):
      stack2.append(stack1.pop()) 
      i += 1
  else:
    array = stack1[-amt:]   
    stack2.extend(array)
    for i in range(amt):
      stack1.pop()

if __name__ == "__main__":
  for path in sys.argv[1:]:
    puzzleInput = parse(path)
    solve(puzzleInput, 1)
    solve(puzzleInput, 2)
