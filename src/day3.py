import string

def day3_1():

    p = 0

    with open('inputs/day3/day3.txt') as f:

        while True:

            line = f.readline()
            if not line:
                break

            line = line.rstrip()
            split_index = int(len(line)/2)
            w1, w2 = line[:split_index], line[split_index:]

            for i in range(split_index):
                if w1[i] in w2:
                    double = w1[i]
                    break
            p += string.ascii_letters.index(double) + 1

        print(f'Sum of priorization: {p}')

def day3_2():

    p = 0
    block_size = 3
    with open('inputs/day3/day3.txt') as f:

        while True:

            block = []
            line = f.readline()
            if not line:
                break
            else:
                block.append(line.rstrip())
                for i in range(block_size - 1):
                    line = f.readline()
                    block.append(line.rstrip())

            for c in block[0]:
                if (c in block[1]) & (c in block[2]):
                    triple = c
                    break

            p += string.ascii_letters.index(triple) + 1

    print(f'Sum of priorization: {p}')