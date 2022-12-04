import functools


def main():
    with open('resources/day4.txt') as r:
        input = r.read()

    pairs = parse(input)

    part1 = sum([fullyContains(pair) for pair in pairs])
    print(part1)

    part2 = sum([overlaps(pair) for pair in pairs])
    print(part2)


def parse(input):
    return [[parseElf(elf) for elf in pair.split(',')] for pair in input.split('\n')]


def parseElf(elf):
    s, e = elf.split('-')
    return set(range(int(s), int(e) + 1))


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
