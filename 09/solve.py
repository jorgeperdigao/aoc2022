f = open("data.txt", "r")
moves=f.read().splitlines()
# moves=[ \
# 'R 4',
# 'U 4',
# 'L 3',
# 'D 1',
# 'R 4',
# 'D 1',
# 'L 5',
# 'R 2']
# moves=[ \
# 'R 5',
# 'U 8',
# 'L 8',
# 'D 3',
# 'R 17',
# 'D 10',
# 'L 25',
# 'U 20']

#  y
# /|\
#  |
#  o---> x
# 
cmds={
    "R":[ 1, 0],
    "L":[-1, 0],
    "U":[ 0, 1],
    "D":[ 0,-1]
}

def get_delta_head(cmd):
    return cmds[cmd]

def get_tail_move(diff_x,diff_y):
    # already touching
    if (1>=abs(diff_x)) and (1>=abs(diff_y)):
        return [0,0]
    # .....    .....
    # .T.H. -> ..TH.
    # .....    .....
    elif (abs(diff_x)==2) and (diff_y==0):
        return [-int(diff_x/abs(diff_x)),0]
    # ...    ...
    # .T.    ...
    # ... -> .T.
    # .H.    .H.
    # ...    ...
    elif (abs(diff_y)==2) and (diff_x==0):
        return [0,-int(diff_y/abs(diff_y))]
    # .....    .....
    # ..H..    ..H..
    # ..... -> ..T..
    # .T...    .....
    # .....    .....
    ################
    # .....    .....
    # .....    .....
    # ...H. -> ..TH.
    # .T...    .....
    # .....    .....
    elif ((abs(diff_x)==2) and (abs(diff_y)==1)) or \
         ((abs(diff_y)==2) and (abs(diff_x)==1)):
        return [-int(diff_x/abs(diff_x)),-int(diff_y/abs(diff_y))]
    # new motion allowed for part 2!
    elif ((abs(diff_x)==2) and (abs(diff_y)==2)):
        return [-int(diff_x/abs(diff_x)),-int(diff_y/abs(diff_y))]
    else:
        print("Unexpected scenario????",diff_x,diff_y)
        return None

def move_once(cmd,pos_h,pos_t):
    #move head first
    delta_head = get_delta_head(cmd)
    pos_h[0] += delta_head[0]
    pos_h[1] += delta_head[1]
    #calculate head move
    tailmove=get_tail_move(pos_t[0]-pos_h[0], pos_t[1]-pos_h[1])
    pos_t[0]+=tailmove[0]
    pos_t[1]+=tailmove[1]
    return (pos_h,pos_t)

def move_tail(pos_h,pos_t):
    tailmove=get_tail_move(pos_t[0]-pos_h[0], pos_t[1]-pos_h[1])
    pos_t[0]+=tailmove[0]
    pos_t[1]+=tailmove[1]
    return (pos_h,pos_t)

def print_map(mapsize,pos_h,pos_t):
    map=[]
    for k in range(mapsize):
        map.append(["."]*mapsize)
    map[pos_t[1]][pos_t[0]]="T"
    map[pos_h[1]][pos_h[0]]="H"
    map.reverse()
    for row in map:
        print("".join(row))

# start pos
pos_head=[0,0]
pos_tail=[0,0]
visited_coordinates=set([(0,0)])

#print_map(6,pos_head,pos_tail)
for move in moves:
    cmd = move[0]
    amount = int(move[2:])
    #print("==",move,"==")
    for k in range(amount):
        (pos_head, pos_tail) = move_once(cmd, pos_head, pos_tail)
        #print_map(6,pos_head,pos_tail)
        #print()
        visited_coordinates.add((pos_tail[0],pos_tail[1]))

print("Part 1:",len(visited_coordinates))


def print_map_tails(mapsize,pos_h,pos_tails):
    map=[]
    for k in range(mapsize):
        map.append(["."]*mapsize)
    for k in range(len(pos_tails)-1,-1,-1):
        tail_x = pos_tails[k][0]
        tail_y = pos_tails[k][1]
        map[tail_y][tail_x]=str(k+1)
    map[pos_h[1]][pos_h[0]]="H"
    map.reverse()
    for row in map:
        print("".join(row))

# start pos
pos_head=[0,0]
pos_tails=[]
for k in range(9):
    pos_tails.append([0,0])
visited_coordinates_t9=set([(0,0)])

#print_map_tails(6,pos_head,pos_tails)

for move in moves:
    cmd = move[0]
    amount = int(move[2:])
    #print("==",move,"==")
    for k in range(amount):
        #print("moving head and tail 1")
        (pos_head,  pos_tails[0]) = move_once(cmd, pos_head, pos_tails[0])
        for m in range(8):
            #print("moving tail",m+2)
            (pos_tails[m], pos_tails[m+1]) = move_tail(pos_tails[m], pos_tails[m+1])
            #print_map_tails(6,pos_head,pos_tails)
        visited_coordinates_t9.add((pos_tails[8][0],pos_tails[8][1]))

print("Part 2:",len(visited_coordinates_t9))