f = open("data.txt", "r")
workpairs=f.read().splitlines()

# workpairs=['2-4,6-8',
# '2-3,4-5',
# '5-7,7-9',
# '2-8,3-7',
# '6-6,4-6',
# '2-6,4-8']

total_overlap_count=0
for pair in workpairs:
    pair_str = pair.split(",")
    rangeA = pair_str[0].split("-")
    rangeB = pair_str[1].split("-")
    A1=int(rangeA[0])
    A2=int(rangeA[1])
    B1=int(rangeB[0])
    B2=int(rangeB[1])

    # ?><?><";'][p`\\]["
    # A contains B
    # A1 <= B1 <= B2 <= A2
    if (A1 <= B1) and (B2 <= A2):
        print("A contains B:",pair)
        total_overlap_count+=1
        continue
    # B contains A
    # B1 <= A1 <= A2 <= B2
    if (B1 <= A1) and (A2 <= B2):
        print("B contains A:",pair)
        total_overlap_count+=1
        continue

print("First part: ", total_overlap_count)

some_overlap_count=0
for pair in workpairs:
    pair_str = pair.split(",")
    rangeA = pair_str[0].split("-")
    rangeB = pair_str[1].split("-")
    A1=int(rangeA[0])
    A2=int(rangeA[1])
    B1=int(rangeB[0])
    B2=int(rangeB[1])

    # ?><?><";'][p`\\]["
    # A and B overlap
    # A1 <= B1 <= A2 <= B2
    # B1 <= A1 <= B2 <= A2 
    if ((A1 <= B1) and (B1 <= A2)) or \
       ((B1 <= A1) and (A1 <= B2)):
        print("A and B overlap:",pair)
        some_overlap_count+=1
        continue

print("Second part: ", some_overlap_count)