eq = {
    'A': ['X','Y','Z'],
    'B': ['Y','Z','X'],
    'C': ['Z','X','Y'],
}

hand_score = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

def day2_1(eq, hand_score):

    with open('inputs/day2/test.txt') as f:
        s = 0
        while True:
            line = f.readline()

            if not line:
                break
            line = line.splitlines()[0].split()

            # hand score
            s += hand_score[line[1]]

            # score of the victory/draw
            if eq[line[0]][0] == line[1]: # draw
                s += 3
            elif eq[line[0]][2] == line[1]: # win
                s += 6
    print(f'Total score: {s}')

def day2_2(eq, hand_score):

    with open('inputs/day2/day2.txt') as f:
        s = 0
        while True:

            line = f.readline()
            if not line:
                break
            line = line.splitlines()[0].split()

            if line[1] == 'Y': # draw
                s += 3 + hand_score[eq[line[0]][0]]
            if line[1] == 'Z':
                s += 6 + hand_score[eq[line[0]][1]]
            if line[1] == 'X':
                s += hand_score[eq[line[0]][2]]

    print(f'Total score: {s}')