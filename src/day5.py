from copy import deepcopy


def main():
    with open('resources/day5.txt') as r:
        input = r.read()

    stacks, procedure = parse(input)

    part1 = part1_fn(deepcopy(stacks), procedure)
    print(part1)

    part2 = part2_fn(deepcopy(stacks), procedure)
    print(part2)


def part1_fn(state, procedure):
    for p in procedure:
        for i in range(p[0]):
            state = move(1, p[1], p[2], state)
    return ''.join([s[-1] for s in state.values()])


def part2_fn(state, procedure):
    for p in procedure:
        state = move(p[0], p[1], p[2], state)
    return ''.join([s[-1] for s in state.values()])


def move(i, f, t, state):
    state[t] = state[t] + state[f][-i:]
    state[f] = state[f][:-i]
    return state


def parse(input):
    raw_stacks, raw_procedure = input.split('\n\n')
    stacks = parseStack(raw_stacks)
    procedure = parseProcedure(raw_procedure)
    return stacks, procedure


def parseStack(raw_stacks):
    rows = raw_stacks.split('\n')
    stacks = {}
    for i in range(1, len(rows[-1]), 4):
        stackNr = rows[-1][i]
        crates = [r[i] for r in reversed(rows[:-1]) if r[i] != ' ']
        stacks[stackNr] = crates
    return stacks


def parseProcedure(raw_procedure):
    rows = [r.split(' ') for r in raw_procedure.split('\n')]
    return [(int(p[1]), p[3], p[5]) for p in rows]


if __name__ == '__main__':
    main()
