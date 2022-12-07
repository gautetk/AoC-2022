from functools import reduce


def main():
    with open('resources/day7.txt') as r:
        input = r.read()

    commands = parse(input)
    files = findFiles(commands)
    folders = folderSizes(files)

    part1 = sum([size for size in folders.values() if size <= 100000])
    print(part1)

    minDeleteSize = 30000000 - 70000000 + folders['/']
    part2 = min([size for size in folders.values() if size >= minDeleteSize])
    print(part2)


def findFiles(commands):
    state = reduce(updateState, commands, {'pwd': ['/'], 'files': []})
    return state['files']


def updateState(state, command):
    c, *lines = command
    if c[0] == 'cd':
        state['pwd'] = cd(c[1], state['pwd'])
    elif c[0] == 'ls':
        state['files'] = state['files'] + ls(state['pwd'], lines)
    return state


def folderSizes(files):
    folders = {}
    for size, pwd in files:
        for i in range(len(pwd)):
            path = '/'.join(pwd[:i + 1])
            folders[path] = folders.get(path, 0) + size
    return folders


def cd(dir, pwd):
    if dir == '..':
        return pwd[:-1]
    elif dir == '/':
        return ['/']
    else:
        return pwd + [dir]


def ls(pwd, files):
    return [(int(size), pwd) for size, _ in files if size != 'dir']


def parse(input):
    return [parseCommand(command_str) for command_str in input.split('$ ') if command_str]


def parseCommand(command_str):
    command_lst = command_str.strip().split('\n')
    return [line.split(' ') for line in command_lst]


if __name__ == '__main__':
    main()
