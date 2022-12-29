times = dict(
    {
    "noop": 1,
    "addx": 2
    }
)

ops = dict()
c = 0

idx = 1
with open("inputs/day10/day10.txt","r") as f:

    for line in f.readlines():

        line = line.split()

        if line[0] == 'addx':
            c = c + times['addx']
            if c in ops.keys():
                ops[c] += int(line[1])
            else:
                ops[c] = int(line[1])
        if line[0] == 'noop':
            c += 1

x = 1
strength = 0
strength_cycle = 20
period_strength_cycle = 40

for idx_op in range(max(ops.keys())):

    if idx_op in ops.keys():
        x += ops[idx_op]
    if idx_op == strength_cycle -1:
        strength += strength_cycle*x
        print(f"{strength_cycle} * {x} = {strength}")
        strength_cycle += period_strength_cycle


print(f"Total strength: {strength}.")
