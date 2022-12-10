f = open("data.txt", "r")
rounds=f.readlines()
print(rounds)

shape_match={"X":"A", "Y":"B", "Z":"C"}
shape_value={"A":1, "B":2, "C":3}

#human_read={"A":"Rock    ","B":"Paper   ","C":"Scissors"}

score_lookup = {
    ("A","A"): 3,
    ("A","B"): 6,
    ("A","C"): 0,
    ("B","A"): 0,
    ("B","B"): 3,
    ("B","C"): 6,
    ("C","A"): 6,
    ("C","B"): 0,
    ("C","C"): 3,
}

def interpret_game_part1(game):
    (opp,you)=game.split()
    you=shape_match[you]
    return (opp,you)


def get_score(game):
    (opp,you)=game
    score=shape_value[you]
    score+=score_lookup[game]
    #print(human_read[opp],"x",human_read[shape_match[you]],"=",score)
    return score

print("Part 1:",sum([get_score(interpret_game_part1(game)) for game in rounds]))

play_lookup = {
    ("A","X"): "C",
    ("A","Y"): "A",
    ("A","Z"): "B",
    ("B","X"): "A",
    ("B","Y"): "B",
    ("B","Z"): "C",
    ("C","X"): "B",
    ("C","Y"): "C",
    ("C","Z"): "A",
}

def interpret_game_part2(game):
    (opp,you)=game.split()
    you=play_lookup[(opp,you)]
    return (opp,you)

print("Part 2:",sum([get_score(interpret_game_part2(game)) for game in rounds]))
