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
  commonItem = ''.join(set(compartment1).intersection(set(compartment2)))
  totalPriorities += getPrioritization(commonItem)

print(totalPriorities)