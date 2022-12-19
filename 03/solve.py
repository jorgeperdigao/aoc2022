f = open("data.txt", "r")
rucksacks=f.readlines()
# rucksacks=['vJrwpWtwJgWrhcsFMMfFFhFp\n',
# 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n',
# 'PmmdzqPrVvPwwTWBwg\n',
# 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n',
# 'ttgJtRGJQctTZtZT\n',
# 'CrZsJsPPZsGzwwsLwLmpwMDw\n']

base_lowerA=int.from_bytes(b"a", "big") # 97
base_upperA=int.from_bytes(b"A", "big") # 65

def getItemPrio(letter):
    if (letter >= base_upperA) and (letter < base_lowerA):
        return letter-base_upperA+27
    elif (letter >= base_lowerA):
        return letter-base_lowerA+1

sumOfMistaskes=0
for rucksack in rucksacks:
    ruckbytes=rucksack.encode('ascii')[0:-1]
    l=len(ruckbytes)
    ruckbytes_1=ruckbytes[:int(l/2)]
    ruckbytes_2=ruckbytes[int(l/2):]
    ruckset1=set(ruckbytes_1)
    ruckset2=set(ruckbytes_2)
    #print(ruckbytes,ruckbytes_1,ruckbytes_2)
    mistake=next(iter(ruckset1.intersection(ruckset2)))
    #print(chr(mistake), getItemPrio(mistake))
    sumOfMistaskes+=getItemPrio(mistake)

print("Part 1:",sumOfMistaskes)

#Part 2

sumOfGroupPrios=0
for index0 in range(0, len(rucksacks), 3):
    #print("index0",index0)
    ruckbytes_1=rucksacks[index0].encode('ascii')[0:-1]
    ruckbytes_2=rucksacks[index0+1].encode('ascii')[0:-1]
    ruckbytes_3=rucksacks[index0+2].encode('ascii')[0:-1]
    ruckset_1=set(ruckbytes_1)
    ruckset_2=set(ruckbytes_2)
    ruckset_3=set(ruckbytes_3)
    #print(ruckbytes_1,ruckbytes_2,ruckbytes_3)
    group = next(iter(ruckset_1.intersection(ruckset_2).intersection(ruckset_3)))
    #print(group,chr(group),getItemPrio(group))
    sumOfGroupPrios += getItemPrio(group)

print("Part 2:", sumOfGroupPrios)