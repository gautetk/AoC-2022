import functools

WIN_SCORE = {
    'A X': 3,
    'A Y': 6,
    'A Z': 0,
    'B X': 0,
    'B Y': 3,
    'B Z': 6,
    'C X': 6,
    'C Y': 0,
    'C Z': 3,
}

XYZ_SCORE = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

WIN_SCORE2 = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

XYZ_SCORE2 = {
    'A X': 3,
    'A Y': 1,
    'A Z': 2,
    'B X': 1,
    'B Y': 2,
    'B Z': 3,
    'C X': 2,
    'C Y': 3,
    'C Z': 1,
}


def main():
    with open('resources/day2.txt') as r:
        input = r.read()

    rows = parse(input)

    part1 = functools.reduce(
        lambda a, b: a + WIN_SCORE[b] + XYZ_SCORE[b[-1]], rows, 0)
    print(part1)

    part2 = functools.reduce(
        lambda a, b: a + XYZ_SCORE2[b] + WIN_SCORE2[b[-1]], rows, 0)
    print(part2)


def parse(input):
    return input.split('\n')


if __name__ == '__main__':
    main()
