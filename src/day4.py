def day4_1():

    c = 0

    with open('inputs/day4/day4.txt') as f:

        for line in f.readlines():

            line = line.rstrip().split(',')
            pair = [s.split('-') for s in line]

            l1 = int(pair[0][0])
            l2 = int(pair[1][0])
            r1 = int(pair[0][1])
            r2 = int(pair[1][1])

            p1_in_p2 = (l1 >= l2) & (r1 <= r2)
            p2_in_p1 = (l1 <= l2) & (r1 >= r2)

            if (p1_in_p2 | p2_in_p1):
                c += 1

        print(f'total overlappings: {c}')

def day4_2():

    c = 0

    with open('inputs/day4/day4.txt') as f:

        for line in f.readlines():

            line = line.rstrip().split(',')
            pair = [s.split('-') for s in line]

            r1 = [*range(int(pair[0][0]), int(pair[0][1]) + 1)]
            r2 = [*range(int(pair[1][0]), int(pair[1][1]) + 1)]

            if True in [r1[i] in r2 for i in range(len(r1))]:
                c += 1

        print(f'total overlappings: {c}')

day4_2()