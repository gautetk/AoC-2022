from functools import reduce


def main():
    with open('resources/day8.txt') as r:
        input = r.read()

    rows = parse(input)
    cols = [list(c) for c in zip(*rows)]

    part1 = part1_fn(rows, cols)
    print(part1)

    part2 = part2_fn(rows, cols)
    print(part2)


def part1_fn(rows, cols):
    visible = 2 * len(rows) + 2 * (len(rows) - 2)
    for r in range(1, len(rows) - 1):
        for c in range(1, len(cols) - 1):
            v = rows[r][c]
            dirs = getDirs(r, c, rows, cols)
            visible += isVisible(v, dirs)
    return visible


def isVisible(v, dirs):
    for dir in dirs:
        if v > max(dir):
            return 1
    return 0


def part2_fn(rows, cols):
    maxScenic = 0
    for r in range(1, len(rows) - 1):
        for c in range(1, len(cols) - 1):
            v = rows[r][c]
            dirs = getDirs(r, c, rows, cols)
            dir_scenic = [calcScenic(v, dir) for dir in dirs]
            scenic = reduce(lambda s, ds: s * ds, dir_scenic, 1)
            if scenic > maxScenic:
                maxScenic = scenic
    return maxScenic


def calcScenic(v, dir):
    for i, h in enumerate(dir):
        if v <= h:
            break
    return i + 1


def getDirs(r, c, rows, cols):
    return [
        rows[r][c-1::-1],
        rows[r][c + 1:],
        cols[c][r-1::-1],
        cols[c][r + 1:],
    ]


def parse(input):
    return [[int(t) for t in row] for row in input.split('\n')]


if __name__ == '__main__':
    main()
