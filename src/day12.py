

def main():
    with open('resources/day12.txt') as r:
        input = r.read()

    start, end, river = parse(input)

    part1 = dijkstra(start, end, river)
    print(part1)

    startLocations = [k for k, v in river.items() if v == 0]
    part2 = min([dijkstra(start, end, river) for start in startLocations])
    print(part2)


def dijkstra(start, end, river):
    visited = set()
    lengths = {start: river.get(start)}

    for _ in range(10000000):
        if len(lengths) == 0:
            return 999999
        currentPos = min(lengths, key=lambda i: lengths[i])
        currentLength = lengths[currentPos]
        currentHeight = river.get(currentPos)
        if currentPos == end:
            return lengths[currentPos]

        visited.add(currentPos)
        del lengths[currentPos]

        for n in neighbors(currentPos, visited):
            if n in river:
                if river.get(n) < currentHeight + 2:
                    d = currentLength + 1
                    if lengths.get(n, 9999999999) > d:
                        lengths[n] = d


def neighbors(n, visited):
    x, y = n
    posLoc = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]

    return [loc for loc in posLoc if loc not in visited]


def parse(input):
    rows = input.split('\n')
    river = {}
    for i, row in enumerate(rows):
        if 'S' in row:
            start = (row.find('S'), i)
            row = row.replace('S', 'a')
        if 'E' in row:
            end = (row.find('E'), i)
            row = row.replace('E', 'z')

        for j, s in enumerate(row):
            river[j, i] = ord(s) - ord('a')

    return start, end, river


if __name__ == '__main__':
    main()
