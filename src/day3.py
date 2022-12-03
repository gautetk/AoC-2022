import functools


def main():
    with open('resources/day3.txt') as r:
        input = r.read()

    sacks = input.split('\n')

    part1 = part1_fn(sacks)
    print(part1)

    part2 = part2_fn(sacks)
    print(part2)


def part1_fn(sacks):
    unique = [intersect(splitInTwo(sack)) for sack in sacks]
    return functools.reduce(lambda v, letter: v + letterToInt(letter), unique, 0)


def splitInTwo(sack):
    return (sack[:len(sack)//2], sack[len(sack)//2:])


def part2_fn(sacks):
    groups = [sacks[i:i + 3] for i in range(0, len(sacks), 3)]
    badges = [intersect(group) for group in groups]
    return functools.reduce(lambda a, b: a + letterToInt(b), badges, 0)


def intersect(listOfStrings):
    intersection = functools.reduce(
        lambda a, b: a & set(b),
        listOfStrings[1:],
        set(listOfStrings[0])
    )
    return list(intersection)[0]


def letterToInt(l):
    if l.isupper():
        return ord(l) - 38
    else:
        return ord(l) - 96


if __name__ == '__main__':
    main()
