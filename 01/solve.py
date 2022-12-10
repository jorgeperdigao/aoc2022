f = open("data.txt", "r")
elves_data=f.read().split("\n\n")
elves_cals=[([int(cals) for cals in elf_data.split("\n")]) for elf_data in elves_data]

cals = [sum(cals) for cals in elves_cals]
cals.sort(reverse=True)
print("Part 1: ", cals[0])
print("Part 2: ", sum(cals[0:3]))