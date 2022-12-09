assignmentPairs = []
with open('day4.txt', 'r') as file:
  lines = file.read().splitlines()
  for line in lines:
    unformattedAssignments = line.split(',')
    assignmentPair = []
    for unformattedAssignment in unformattedAssignments:
      rangeValues = unformattedAssignment.split('-')
      assignment = list(range(int(rangeValues[0]), int(rangeValues[1]) + 1))
      assignmentPair.append(assignment)
    assignmentPairs.append(assignmentPair)

total = 0
for assignmentPair in assignmentPairs:
  if all(section in assignmentPair[1] for section in assignmentPair[0]) or all(section in assignmentPair[0] for section in assignmentPair[1]):
    total += 1
print(total)

total = 0
for assignmentPair in assignmentPairs:
  if any(section in assignmentPair[1] for section in assignmentPair[0]):
    total += 1
print(total)