f = open("data.txt", "r")
datastream=f.readlines()
#datastream = ['zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw']

def find_start_of_packet(datastream):
    if(len(datastream) >= 4):
        for pos in range(len(datastream)-4+1):
            window = [datastream[pos+win_k] for win_k in (range(4))]
            group = set(window)
            # print(window)
            # print(group)
            if(len(group)==4):
                return pos+4

print("Part 1:", find_start_of_packet(datastream[0]))

def find_start_of_msg(datastream):
    if(len(datastream) >= 14):
        for pos in range(len(datastream)-14+1):
            window = [datastream[pos+win_k] for win_k in (range(14))]
            group = set(window)
            # print(window)
            # print(group)
            if(len(group)==14):
                return pos+14

print("Part 2:", find_start_of_msg(datastream[0]))