from pprint import pprint




def main():
    with open('resources/day7.txt') as r:
        input = r.read()

    commands = parse(input)



    pwd = '/'
    tree = {
        '/': [],
    }

    tree = findTree(commands, pwd, tree)
        
    pprint(tree)
    

    # part1 = sum([fullyContains(pair) for pair in pairs])
    # print(part1)

    # part2 = sum([overlaps(pair) for pair in pairs])
    # print(part2)

def findTree(commands, pwd, tree):
    COM = {
        'cd': cd,
        'ls': ls,
    }
    for c in commands:
        pwd, tree = COM[c[0][0]](c, pwd, tree)
    return tree
        
    
def cd(c, pwd, tree):
    pwd = c[0][1]
    return pwd, tree
    
def ls(c, pwd, tree):
    for loc in c[1:]:
        tree[pwd] = tree.get(pwd, []) + [loc]
    return pwd, tree


def fullyContains(pair):
    intersect = pair[0] & pair[1]
    if intersect in pair:
        return 1
    return 0


def overlaps(pair):
    if pair[0] & pair[1]:
        return 1
    return 0



def parse(input):
    return [parseCommand(command_str) for command_str in input.split('$ ') if command_str]

def parseCommand(command_str):
    command_lst = command_str.strip().split('\n')
    return [line.split(' ') for line in command_lst]

if __name__ == '__main__':
    main()
