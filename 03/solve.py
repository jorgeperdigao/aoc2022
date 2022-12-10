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

print(sumOfMistaskes)