import re

f = open("data.txt", "r")
bashhistory=f.read().splitlines()
# bashhistory=['$ cd /',
#            '$ ls',
#            'dir a',
#            '14848514 b.txt',
#            '8504156 c.dat',
#            'dir d',
#            '$ cd a',
#            '$ ls',
#            'dir e',
#            '29116 f',
#            '2557 g',
#            '62596 h.lst',
#            '$ cd e',
#            '$ ls',
#            '584 i',
#            '$ cd ..',
#            '$ cd ..',
#            '$ cd d',
#            '$ ls',
#            '4060174 j',
#            '8033020 d.log',
#            '5626152 d.ext',
#            '7214296 k']

class LsCmd:
    pass

def get_cd_target(line):
    m_cd = re.search('\$ cd (.*)$', line)
    if m_cd is not None:
        return(m_cd.group(1))
    elif (line == '$ ls'):
        return None #LsCmd()
    else:
        warning("oops")

# I could just have a vector of pointers, but this is what I started with...
def get_pointer_from_dirstack(dirstack, filemap):
    pointer = filemap
    for dir in dirstack:
        pointer = pointer[dir]
    return pointer

def update_all_dirs_size(dir_stack,filesize):
    for pointer in dir_stack:
        if "__SIZE__" in pointer.keys():
            pointer["__SIZE__"]+=filesize
        else:
            pointer["__SIZE__"]=filesize

def shell2dict(shell_hist):
    dir_stack=[]
    filemap={"/":{}}
    pointer=filemap

    for line in shell_hist:
        # print("###","'"+line+"'")
        # interpret cd commands
        if line[0] == "$":
            cd_target=get_cd_target(line)
            if(cd_target is not None):
                if(cd_target == ".."):
                    #dir_stack.pop()
                    #deprecated# pointer=get_pointer_from_dirstack(dir_stack, filemap)
                    dir_stack.pop()
                    pointer=dir_stack[-1]
                else:
                    #deprecated# dir_stack.append(cd_target)
                    pointer=pointer[cd_target]
                    dir_stack.append(pointer)
        # create directories
        elif line.startswith("dir"):
            dirname_match = re.search('dir (.*)$', line)
            dirname=dirname_match.group(1)
            if dirname not in pointer.keys():
                pointer[dirname]={}
        # create files
        else:
            m_size = re.search('([0-9]+) (.*)$', line)
            if(m_size is not None):
                filesize=int(m_size.group(1))
                filename=m_size.group(2)
                # print("file",filename,"=",filesize)
                pointer[filename]=filesize
            else:
                warning("oops")
            update_all_dirs_size(dir_stack,filesize)
        
        #print("stack depth",len(dir_stack))
        #print(pointer)
    return filemap

filemap=shell2dict(bashhistory)
print(filemap)

def get_part1_heuristic(rest_of_disk):
    retSum=0
    for name in rest_of_disk.keys():
        pointer=rest_of_disk[name]
        if isinstance(pointer,dict):
            retSum+=get_part1_heuristic(pointer)
        elif name == "__SIZE__":
            if pointer < 100000:
                retSum+=pointer
    return retSum

print("Part 1:",get_part1_heuristic(filemap))
max_used_disk=40000000
cur_used_disk=filemap["/"]["__SIZE__"]
diff_to_delete=cur_used_disk-max_used_disk
print("Used disk:",cur_used_disk)
print("Need to delete:",diff_to_delete)

def find_best_match_dir(rest_of_disk,needed_space,stack):
    this_dir_size=rest_of_disk["__SIZE__"]

    if (this_dir_size<needed_space):
        return (None,None)
    
    best_match=this_dir_size
    best_stack=stack

    for name in rest_of_disk.keys():
        pointer=rest_of_disk[name]
        if isinstance(pointer,dict):
            (alternative, alt_stack)=find_best_match_dir(pointer,needed_space,stack+[name])
            if alternative is not None:
                if(alternative < best_match):
                    best_match=alternative
                    best_stack=alt_stack
                    print("new best:",best_match,best_match-needed_space,best_stack)
    return (best_match, best_stack)


print("Part 2:",find_best_match_dir(filemap["/"],diff_to_delete, ["/"]))
