rucksacks = []
with open('day3.txt', 'r') as file:
  rucksacks = file.read().splitlines()

def getPrioritization(item):
  itemUnicode = ord(item)
  if itemUnicode >= ord('a'):
    return itemUnicode - ord('a') + 1
  else:
    return itemUnicode - ord('A') + 27

totalPriorities = 0
for rucksack in rucksacks:
  compartment1 = rucksack[slice(0, len(rucksack)//2)]
  compartment2 = rucksack[slice(len(rucksack)//2, len(rucksack))]
  commonItem = ''.join(set(compartment1) & set(compartment2))
  totalPriorities += getPrioritization(commonItem)
print(totalPriorities)

totalPriorities = 0
for i in range(0, len(rucksacks), 3):
  rucksack1, rucksack2, rucksack3 = rucksacks[i], rucksacks[i+1], rucksacks[i+2]
  commonItem = ''.join(set(rucksack1) & set(rucksack2) & set(rucksack3))
  totalPriorities += getPrioritization(commonItem)
print(totalPriorities)