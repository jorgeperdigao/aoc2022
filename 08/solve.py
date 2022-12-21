f = open("data.txt", "r")
treemap=f.read().splitlines()
# treemap=['30373',
#          '25512',
#          '65332',
#          '33549',
#          '35390']

def rolling_and(vector):
    for booly in vector:
        if not booly:
            return False
    return True

def get_matrix_from_trees(lines):
    return [[int(c) for c in line] for line in lines]
        
def check_tree_in_line(pos,line):
    # tree is only visible if at least one tree is smaller
    mytree=line[pos]
    trees2left=line[:pos]
    trees2right=line[(pos+1):]
    left_visible=rolling_and([(mytree > other_tree) for other_tree in trees2left])
    right_visible=rolling_and([(mytree > other_tree) for other_tree in trees2right])
    # print("up/left    ->",left_visible)
    # print("down/right ->",right_visible)
    return (left_visible or right_visible)

#O--> x
#|
#v y
def is_tree_visible(pos_x, pos_y, tree_matrix):
    # print("Checking tree",pos_x,pos_y,"with height",tree_matrix[pos_y][pos_x])
    dim_x=len(tree_matrix[0])
    dim_y=len(tree_matrix)
    if (pos_x == 0) or \
       (pos_x == (dim_x-1)) or \
       (pos_y == 0) or \
       (pos_y == (dim_y-1)):
       return 1
    # print("horiz:")
    horiz=check_tree_in_line(pos_x,tree_matrix[pos_y])
    # print("verti:")
    verti=check_tree_in_line(pos_y,[tree_matrix[y][pos_x] for y in range(dim_y)])
    return 1 if (horiz or verti) else 0


tree_matrix=get_matrix_from_trees(treemap)

dim_x=len(tree_matrix[0])
dim_y=len(tree_matrix)

sum_visible_trees=0
for x in range(dim_x):
    for y in range(dim_y):
        sum_visible_trees+=is_tree_visible(x,y,tree_matrix)
print("Part 1:",sum_visible_trees)

#########################################################

def count_trees_visible(treehouse,treeline,invert=False):
    if(invert):
        treeline.reverse()

    count=0
    for tree in treeline:
        count+=1
        if tree >= treehouse:
            break

    # WTF higher trees don't block lower following trees????
    # #print(treeline)
    # count=1
    # if(len(treeline) > 1):
    #     curr_tree_height=treeline[0]
    #     if curr_tree_height >= treehouse:
    #         return 1
    #     for newtree in treeline[1:]:
    #         if (newtree < curr_tree_height):
    #             break
    #         curr_tree_height = newtree
    #         count+=1
    return count

def calculate_scenic_score(pos_x, pos_y, tree_matrix):
    dim_x=len(tree_matrix[0])
    dim_y=len(tree_matrix)
    if (pos_x == 0) or \
       (pos_x == (dim_x-1)) or \
       (pos_y == 0) or \
       (pos_y == (dim_y-1)):
       return [0]

    mytree=tree_matrix[pos_y][pos_x]
    
    
    left_count = count_trees_visible(mytree,tree_matrix[pos_y][:pos_x],invert=True)
    #print("left_count =",left_count)
    right_count = count_trees_visible(mytree,tree_matrix[pos_y][(pos_x+1):])
    #print("right_count =",right_count)

    vertical_treeline=[tree_matrix[y][pos_x] for y in range(dim_y)]
    up_count = count_trees_visible(mytree,vertical_treeline[:pos_y],invert=True)
    #print("up_count =",up_count)
    down_count = count_trees_visible(mytree,vertical_treeline[(pos_y+1):])
    #print("down_count =",down_count)
    return [(left_count * right_count * up_count * down_count), \
             left_count, \
             right_count, \
             up_count, \
             down_count, \
             tree_matrix[pos_y][:pos_x], \
             tree_matrix[pos_y][(pos_x+1):], \
             vertical_treeline[:pos_y], \
             vertical_treeline[(pos_y+1):] \
             ]

best_scenic_score=0
for y in range(dim_y):
    for x in range(dim_x):
        #print("######")
        #print("y="+str(y),"x="+str(x))
        score_w_details=calculate_scenic_score(x,y,tree_matrix)
        this_scenic_score=score_w_details[0]
        #print("score="+str(this_scenic_score))
        if this_scenic_score > best_scenic_score:
            best_scenic_score = this_scenic_score
            print("New best score at y="+str(y)+",x="+str(x)+":",this_scenic_score)
            left_view=score_w_details[5]
            left_view.reverse()
            up_view=score_w_details[7]
            up_view.reverse()
            print("left :",score_w_details[1],left_view)
            print("right:",score_w_details[2],score_w_details[6])
            print("up   :",score_w_details[3],up_view)
            print("down :",score_w_details[4],score_w_details[8])
print("Part 2:",best_scenic_score)