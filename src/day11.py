from functools import reduce
import math
import copy


def main():
    with open('resources/day11.txt') as r:
        input = r.read()

    monkeys = parse(input)

    worryFn = lambda w: int(w / 3)
    count = doCommands(monkeys, 20, worryFn)
    twoHighest = sorted(count.values())[-2:]
    part2 = reduce(lambda a, b: a * b, twoHighest)
    print(part2)


    lcm = math.lcm(*[m['divisible'] for m in monkeys])
    worryFn = lambda w: w % lcm
    count = doCommands(monkeys, 10000, worryFn)
    twoHighest = sorted(count.values())[-2:]
    part2 = reduce(lambda a, b: a * b, twoHighest)
    print(part2)



def doCommands(monkeys, rounds, worryFn):
    monkeys = copy.deepcopy(monkeys)
    state = {m['nr']: m['si'] for m in monkeys}
    count = {m['nr']: 0 for m in monkeys}

    def wrapper(state_count, m):
        return turn(worryFn, state_count, m)
    
    for _ in range(rounds):
        state, count = reduce(wrapper, monkeys, (state, count))
    return count


def turn(worryFn, state_count, m):
    state, count = state_count
    count[m['nr']] += len(state[m['nr']])
    for w in state[m['nr']]:
        w = m['o_fn'](w)
        w = worryFn(w)
        if checkThrow(w, m):
            state[m['ifTrue']] += [w]
        else:
            state[m['ifFalse']] += [w]
    state[m['nr']] = []
    return state, count


def checkThrow(w, m):
    return w % m['divisible'] == 0


def parse(input):
    return [parseMonkey(monkeyRaw) for monkeyRaw in input.split('\n\n')]


def parseMonkey(monkeyRaw):
    rows = monkeyRaw.split('\n')
    return {
        'nr': rows[0][-2],
        'si': parseStartItems(rows[1]),
        'o_fn': parseOperationFn(rows[2]),
        "divisible": int(rows[3].split('by ')[-1]),
        "ifTrue": rows[4].split('monkey ')[-1],
        "ifFalse": rows[5].split('monkey ')[-1],
        'count': 0,
    }


def parseStartItems(si):
    raw_items = si.split(': ')[1]
    return [int(a) for a in raw_items.split(', ')]


def parseOperationFn(o):
    str_fn = o.split('= ')[1]
    a, operator, b = str_fn.split(' ')
    if '+' == operator:
        def fn(x, y): return x + y
    elif '*' == operator:
        def fn(x, y): return x * y

    if a == 'old' and b == 'old':
        return lambda old: fn(old, old)
    elif a == 'old' and b != 'old':
        b = int(b)
        return lambda old: fn(old, b)
    elif a != 'old' and b == 'old':
        a = int(a)
        return lambda old: fn(a, old)


if __name__ == '__main__':
    main()
