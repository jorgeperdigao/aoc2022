f = open("data.txt", "r")
instructions=f.read().splitlines()
# instructions=[ \
# 'addx 15', 'addx -11',
# 'addx 6','addx -3','addx 5','addx -1','addx -8','addx 13','addx 4',
# 'noop','addx -1','addx 5','addx -1','addx 5','addx -1','addx 5','addx -1',
# 'addx 5','addx -1','addx -35','addx 1','addx 24','addx -19','addx 1',
# 'addx 16','addx -11','noop','noop','addx 21','addx -15','noop','noop',
# 'addx -3','addx 9','addx 1','addx -3','addx 8','addx 1','addx 5','noop',
# 'noop','noop','noop','noop','addx -36','noop','addx 1','addx 7','noop',
# 'noop','noop','addx 2','addx 6','noop','noop','noop','noop','noop','addx 1',
# 'noop','noop','addx 7','addx 1','noop','addx -13','addx 13','addx 7','noop',
# 'addx 1','addx -33','noop','noop','noop','addx 2','noop','noop','noop',
# 'addx 8','noop','addx -1','addx 2','addx 1','noop','addx 17','addx -9',
# 'addx 1','addx 1','addx -3','addx 11','noop','noop','addx 1','noop','addx 1',
# 'noop','noop','addx -13','addx -19','addx 1','addx 3','addx 26','addx -30',
# 'addx 12','addx -1','addx 3','addx 1','noop','noop','noop','addx -9',
# 'addx 18','addx 1','addx 2','noop','noop','addx 9','noop','noop','noop',
# 'addx -1','addx 2','addx -37','addx 1','addx 3','noop','addx 15',
# 'addx -21','addx 22','addx -6','addx 1','noop','addx 2','addx 1','noop',
# 'addx -10','noop','noop','addx 20','addx 1','addx 2','addx 2','addx -6',
# 'addx -11','noop','noop','noop']

def process_cycle(cycle,x):
    print("cycle",cycle,": x =",x)
    if(cycle==20) or ((cycle-20) % 40 == 0):
        print("Signal strength:",cycle*x)
        return(cycle*x)
    return 0

x=1
cycle=1
sigstrength_sum=0

for instr in instructions:
    if instr == "noop":
        print("### noop")
        sigstrength_sum+=process_cycle(cycle,x)
        cycle += 1
    elif instr.startswith("addx"):
        print("### addx")
        sigstrength_sum+=process_cycle(cycle,x)
        cycle += 1
        sigstrength_sum+=process_cycle(cycle,x)
        delta=int(instr[4:])
        x+=delta
        cycle += 1

print("Part 1:", sigstrength_sum)
print("########################")


def render_pixel(cycle,x):
    crt_pos=(cycle-1) % 40
    sprite_lower=x-1
    sprite_upper=x+1
    char="." 
    if(crt_pos >= sprite_lower) and (crt_pos <= sprite_upper):
        char = "#"
    #print(char, end="")
    #if (cycle % 40 == 0):
    #    print()
    return char

x=1
cycle=1
screen=[]

for instr in instructions:
    if instr == "noop":
        print("### noop")
        process_cycle(cycle,x)
        screen.append(render_pixel(cycle,x))
        cycle += 1
    elif instr.startswith("addx"):
        print("### addx")
        process_cycle(cycle,x)
        screen.append(render_pixel(cycle,x))
        cycle += 1
        process_cycle(cycle,x)
        screen.append(render_pixel(cycle,x))
        delta=int(instr[4:])
        x+=delta
        cycle += 1

count=0
for char in screen:
    count+=1
    print(char, end="")
    if (count % 40 == 0):
        print()