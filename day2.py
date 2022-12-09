guide = []
with open('day2.txt', 'r') as file:
  lines = file.read().splitlines()
  guide = list(map(lambda line: line.split(' '), lines))

rock, paper, scissors = 1, 2, 3
win, draw, loss = 6, 3, 0
shapeCodes = {
  'A': rock, 'X': rock,
  'B': paper, 'Y': paper,
  'C': scissors, 'Z': scissors
}
winCodes = {
  'X': loss,
  'Y': draw,
  'Z': win
}
shapeSolutions = {
  scissors: rock,
  rock: paper,
  paper: scissors
}

def shoot(opponentShape, myShape):
  if opponentShape == myShape:
    return draw
  elif shapeSolutions[opponentShape] == myShape:
    return win
  else:
    return loss

def findShape(opponentShape, winCode):
  if winCode == win:
    return shapeSolutions[opponentShape]
  elif winCode == loss:
    possibleSolutions = [rock, paper, scissors]
    possibleSolutions.remove(opponentShape)
    possibleSolutions.remove(shapeSolutions[opponentShape])
    return possibleSolutions[0]
  else:
    return opponentShape

# Part One
results = []
total = 0
for [opponentShapeCode, myShapeCode] in guide:
  opponentShape = shapeCodes[opponentShapeCode]
  myShape = shapeCodes[myShapeCode]
  roundValue = myShape + shoot(opponentShape, myShape)
  results.append(roundValue)
  total += roundValue
print(total)

# Part Two
results = []
total = 0
for [opponentShapeCode, winCode] in guide:
  opponentShape = shapeCodes[opponentShapeCode]
  winValue = winCodes[winCode]
  myShape = findShape(opponentShape, winValue)
  roundValue = myShape + winValue
  results.append(roundValue)
  total += roundValue
print(total)