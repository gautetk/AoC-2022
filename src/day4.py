import functools


def main():
    with open('resources/day4.txt') as r:
        input = r.read()

    parsed = parse(input)

    part1 = part1_fn(parsed)
    print(part1)

    part2 = part2_fn(parsed)
    print(part2)


def parse(input):
    return [[[int(s) for s in elf.split('-')] for elf in pair.split(',')] for pair in input.split('\n')]


def part1_fn(pairs):
    return functools.reduce(lambda total, pair: total + fullyContains(pair), pairs, 0)


def part2_fn(pairs):
    return functools.reduce(lambda total, pair: total + overlaps(pair), pairs, 0)


def fullyContains(pair):
    elf1, elf2 = pair
    if elf1[0] >= elf2[0] and elf1[1] <= elf2[1]:
        return 1
    if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
        return 1
    return 0


def overlaps(pair):
    elf1, elf2 = pair
    if elf1[1] < elf2[0] or elf2[1] < elf1[0]:
        return 0
    return 1


if __name__ == '__main__':
    main()
