import re 
f = open("data.txt", "r")
instructions=f.read().splitlines()

# instructions= \
# ['    [D]    ',
#  '[N] [C]    ',
#  '[Z] [M] [P]',
#  ' 1   2   3 ',
#  '',
#  'move 1 from 2 to 1',
#  'move 3 from 1 to 3',
#  'move 2 from 2 to 1',
#  'move 1 from 1 to 2']


def get_crane_setup(input):

    pile_depth=0
    for line in input:
        if len(line) and (line[1] == "1"):
            break
        pile_depth+=1
    col_count=int((len(input[0])+1)/4)
    crane_setup=[]
    for k in range(col_count):
        crane_setup.append(list())

    for line in input:
        if len(line) and (line[1] == "1"):
            break
        for col in range(col_count):
            idx=1+col*4
            letter=line[idx]
            if letter == " ":
                continue
            crane_setup[col].insert(0, letter)
    return crane_setup

def get_instructions_to_obj(input):
    crane_mode=True
    cmds=[]
    for line in input:
        if crane_mode:
            if line == "":
                crane_mode=False
            continue
        m_cmd = re.search('move ([0-9]+) from ([0-9]+) to ([0-9]+)$', line)
        move_qty   = int(m_cmd.group(1))
        source_grp = int(m_cmd.group(2))-1
        target_grp = int(m_cmd.group(3))-1
        cmds.append((move_qty,source_grp,target_grp))
    return cmds

crane_setup=get_crane_setup(instructions)
#print(crane_setup)
cmds=get_instructions_to_obj(instructions)

for cmd in cmds:
    #print(cmd)
    move_qty   = cmd[0]
    source_grp = cmd[1]
    target_grp = cmd[2]
    loader=[]
    for k in range(move_qty):
        loader.append(crane_setup[source_grp].pop())
        crane_setup[target_grp].append(loader.pop())
    #print(crane_setup)

#print(crane_setup)
code=""
for col in crane_setup:
    code+=col[-1]
print("First part:", code)


crane_setup=get_crane_setup(instructions)
for cmd in cmds:
    # print(crane_setup)
    # print(cmd)
    move_qty   = cmd[0]
    source_grp = cmd[1]
    target_grp = cmd[2]
    loader=[]
    for k in range(move_qty):
        loader.append(crane_setup[source_grp].pop())
    for k in range(move_qty):
        crane_setup[target_grp].append(loader.pop())

#print(crane_setup)
code=""
for col in crane_setup:
    code+=col[-1]
print("Second part:", code)
