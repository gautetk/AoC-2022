from functools import reduce

MOVE = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}


def main():
    with open('resources/day9.txt') as r:
        input = r.read()

    directions = parse(input)

    part1 = tailMovement(directions, 2)
    print(part1)

    part2 = tailMovement(directions, 10)
    print(part2)


def tailMovement(directions, n):
    state = {
        'knots': [(0, 0)]*n,
        "locs": set(),
    }
    state = reduce(step, directions, state)
    return len(state['locs'])


def step(state, d):
    old_knots = state['knots']
    head = [sum(x) for x in zip(old_knots[0], MOVE[d])]
    knots = [head]
    for t in old_knots[1:]:
        knots += [tail(knots[-1], t)]

    state['knots'] = knots
    state['locs'].add(knots[-1])
    return state


def tail(h, t):
    x = h[0] - t[0]
    y = h[1] - t[1]
    if max((abs(x), abs(y))) < 2:
        return t
    elif abs(x) > 1 and y == 0:
        return t[0] + sign(x), t[1]
    elif abs(y) > 1 and x == 0:
        return t[0], t[1] + sign(y)
    else:
        return t[0] + sign(x), t[1] + sign(y)


def sign(v):
    return v/abs(v)


def parse(input):
    commands = []
    for row in input.split('\n'):
        d, n = row.split(' ')
        commands += [d]*int(n)
    return commands


if __name__ == '__main__':
    main()
