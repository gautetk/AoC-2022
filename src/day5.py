import functools


def main():
    with open('resources/day5.txt') as r:
        input = r.read()

    pairs = parse(input)

    # part1 = sum([fullyContains(pair) for pair in pairs])
    # print(part1)

    # part2 = sum([overlaps(pair) for pair in pairs])
    # print(part2)


def parse(input):
    raw_stacks, raw_procedure = input.split('\n\n')
    stacks = parseStack(raw_stacks)
    procedure = parseProcedure(raw_procedure)
    print(procedure)
    # return [[parseElf(elf) for elf in pair.split(',')] for pair in input.split('\n')]

def parseStack(raw_stacks):
    rows = raw_stacks.split('\n')
    stacks = {}
    for i in range(1, len(rows[-1]), 4):
        nr = rows[-1][i]
        crates = [r[i] for r in reversed(rows[:-1]) if r[i] != ' ']
        stacks[nr] = crates
    return stacks
    

def parseProcedure(raw_procedure):
    rows = [r.split(' ') for r in raw_procedure.split('\n')]
    return [(int(p[1]), p[3], p[5]) for p in rows]


def fullyContains(pair):
    intersect = pair[0] & pair[1]
    if intersect in pair:
        return 1
    return 0


def overlaps(pair):
    if pair[0] & pair[1]:
        return 1
    return 0


if __name__ == '__main__':
    main()
