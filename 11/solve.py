f = open("data.txt", "r")
monkey_setup=f.read().splitlines()

#example_
monkey_setup = [ \
'Monkey 0:',
'  Starting items: 79, 98',
'  Operation: new = old * 19',
'  Test: divisible by 23',
'    If true: throw to monkey 2',
'    If false: throw to monkey 3',
'',
'Monkey 1:',
'  Starting items: 54, 65, 75, 74',
'  Operation: new = old + 6',
'  Test: divisible by 19',
'    If true: throw to monkey 2',
'    If false: throw to monkey 0',
'',
'Monkey 2:',
'  Starting items: 79, 60, 97',
'  Operation: new = old * old',
'  Test: divisible by 13',
'    If true: throw to monkey 1',
'    If false: throw to monkey 3',
'',
'Monkey 3:',
'  Starting items: 74',
'  Operation: new = old + 3',
'  Test: divisible by 17',
'    If true: throw to monkey 0',
'    If false: throw to monkey 1']

def read_monkey_setup(lines):
    monkeys=[]
    m=-1 # monkey index
    for line in lines:
        if line == "":
            continue
        elif line.startswith("Monkey"):
            monkeys.append(dict())
            m+=1
            print("# Monkey",m)
        elif line.startswith("  Starting items:"):
            items=[int(k) for k in line[18:].split(",")]
            print("    Items:",items)
            monkeys[m]["items"]=items
            monkeys[m]["inspect_count"]=0
        elif line.startswith("  Operation:"):
            op=line[13:]
            print("    Operation: '"+op+"'")
            monkeys[m]["op"]=op
        elif line.startswith("  Test:"):
            divisibleby=int(line[21:])
            print("    DivBy:",divisibleby)
            monkeys[m]["divby"]=divisibleby
        elif line.startswith("    If true"):
            true_monkey=int(line[29:])
            print("    TMonkey:",true_monkey)
            monkeys[m]["tmonkey"]=true_monkey
        elif line.startswith("    If false"):
            false_monkey=int(line[30:])
            print("    FMonkey:",false_monkey)
            monkeys[m]["fmonkey"]=false_monkey
    
    return monkeys

def do_monkey_round(monkeys, very_worried=False):
    for m, monkey in enumerate(monkeys):
        #print("Monkey",m)
        monkey["items"].reverse() #not required, just to make it similar to example
        while monkey["items"]:
            monkey["inspect_count"]+=1
            item = monkey["items"].pop()
            #print("  Monkey inspects an item with a worry level of ",item)
            #print(monkey["op"])
            _locals = {"old": item}
            exec(monkey["op"], {}, _locals)
            new_item = _locals["new"]
            #print("  New worry level of item is ",new_item)
            if(not very_worried):
                new_item = int(new_item/3)
                #print("  New worry level of item is ",new_item)
            next_monkey = -1
            if (new_item % monkey["divby"]) == 0:
                next_monkey = monkey["tmonkey"]
            else:
                next_monkey = monkey["fmonkey"]
            #print("  Next monkey is:",next_monkey)
            if "next_items" in monkeys[next_monkey].keys():
                monkeys[next_monkey]["next_items"].append(new_item)
            else:
                monkeys[next_monkey]["next_items"] = [new_item]
        for monkey in monkeys:
            if "next_items" in monkey.keys():
                monkey["items"] += monkey["next_items"]
                monkey.pop('next_items', None)
    return monkeys


monkeys = read_monkey_setup(monkey_setup)
print("########")


for round_index in range(20):
    #print("### Round",round_index+1,"###")
    monkeys = do_monkey_round(monkeys)
    for m, monkey in enumerate(monkeys):
        #print("Monkey",m,":",monkey["items"])
        pass

monkey_scores = sorted([monkey["inspect_count"] for monkey in monkeys])
print(monkey_scores)
monkey_scores.reverse()
print("Part 1:", monkey_scores[0]*monkey_scores[1])

#### second part

# OMG the numbers are exploding!! I have to do something about that
for round_index in range(10000):
    monkeys = do_monkey_round(monkeys,very_worried=True)
    print("### Round",round_index+1,"###")
    if True: #if (round_index % 1000) == 0:
        print("### Round",round_index+1,"###")
        for m, monkey in enumerate(monkeys):
            print("Monkey",m,":",monkey["inspect_count"],monkey["items"])