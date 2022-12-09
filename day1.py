inventories = []

with open('day1.txt', 'r') as file:
  input = file.read()
  unsplitInventories = input.split('\n\n')
  for unsplitInventory in unsplitInventories:
    splitInventory = unsplitInventory.split('\n')
    formattedInventory = list(map(lambda food: int(food), splitInventory))
    inventories.append(formattedInventory)

totals = list(map(lambda inventory: sum(inventory), inventories))
totals.sort(reverse=True)
print(totals[0])
print(totals[0] + totals[1] + totals[2])