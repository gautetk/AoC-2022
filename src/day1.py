
def main():
    with open('resources/day1.txt') as r:
        input = r.read()

    elves = parse(input)

    part1 = max(elves)
    print(part1)

    part2 = sum(sorted(elves)[-3:])
    print(part2)


def parse(input):
    return [calCount(elf) for elf in input.split('\n\n')]

def calCount(elf):
    return sum([int(cal) for cal in elf.split('\n')])

if __name__ == '__main__':
    main()
