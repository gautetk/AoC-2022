from functools import reduce


def main():
    with open('resources/day10.txt') as r:
        input = r.read()

    commands = parse(input)

    values = doCommands(commands)

    part1 = part1_fn(values)
    print(part1)

    part2 = part2_fn(values)
    print(part2)


def doCommands(commands):
    state = {
        'x': 1,
        'values': [],
    }

    state = reduce(doCommand, commands, state)
    return state['values']


def doCommand(state, c):
    if c[0] == 'noop':
        state['values'] += [state['x']]
    elif c[0] == 'addx':
        state['values'] += [state['x']]*2
        state['x'] += int(c[1])
    return state


def part1_fn(values):
    locs = [20 + i * 40 for i in range(6)]
    return reduce(lambda tot, n: tot + values[n-1] * n, locs, 0)


def part2_fn(values):
    text = ''
    for i, v in enumerate(values):
        text += draw(v, i)

    return '\n'.join([text[i:i+40] for i in range(0, len(text), 40)])


def draw(x, i):
    i = i % 40
    if i in [x - 1, x, x + 1]:
        return '#'
    return ' '


def parse(input):
    return [row.split(' ') for row in input.split('\n')]


def parseRow(row):
    return (row[0], int(row[1]))


if __name__ == '__main__':
    main()
