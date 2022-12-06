def main():
    with open('resources/day6.txt') as r:
        input = r.read()

    part1 = findFirstUniqueString(input, 4)
    print(part1)

    part2 = findFirstUniqueString(input, 14)
    print(part2)


def findFirstUniqueString(input, n):
    for i in range(n, len(input)):
        if len(set(input[i-n:i])) == n:
            return i


if __name__ == '__main__':
    main()
