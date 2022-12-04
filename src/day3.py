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
    count = 0
    for sack in sacks:
        compartments = [
            set(sack[:len(sack)//2]),
            set(sack[len(sack)//2:]),
        ]
        letter = set.intersection(*compartments)
        count += letterToInt(list(letter)[0])
    return count


def part2_fn(sacks):
    count = 0
    for i in range(0, len(sacks), 3):
        group = [set(elf) for elf in sacks[i:i + 3]]
        letter = set.intersection(*group)
        count += letterToInt(list(letter)[0])
    return count


def letterToInt(l):
    if l.isupper():
        return ord(l) - ord('A') + 27
    else:
        return ord(l) - ord('a') + 1


if __name__ == '__main__':
    main()
