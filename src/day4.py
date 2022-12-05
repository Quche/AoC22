c = 0

with open('inputs/day4/day4.txt') as f:

    i = 0
    for line in f.readlines():

        line = line.rstrip().split(',')
        pair = [s.split('-') for s in line]

        l1 = int(pair[0][0])
        l2 = int(pair[1][0])
        r1 = int(pair[0][1])
        r2 = int(pair[1][1])

        if (l1 > r1):
            print(f'{pair}: l1 is {pair[0][0]}; r1 is {pair[0][1]}: {i}')

        p1_in_p2 = (l1 <= l2) & (r1 <= r2)
        p2_in_p1 = (l2 <= l1) & (r2 <= r1)

        if (p1_in_p2 | p2_in_p1):
            c += 1
        i += 1

    print(f'total overlappings: {c}')