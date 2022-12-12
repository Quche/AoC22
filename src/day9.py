import math

S = [0,0]
H = [S]
T = [S]

def unique(my_list):
    unique_el = []
    for l in my_list:
        if l not in unique_el:
            unique_el.append(l)
    return unique_el

def dist(T,H):
    return math.sqrt((T[0]+H[0])**2 + (T[1]+H[1])**2)


with open('inputs/day9/test.txt') as f:

    for idx, line in enumerate(f.readlines()):
        move = line.rstrip().split(' ')
        for inc in range(int(move[1])):

            # Head
            if move[0] == 'R':
                H.append([H[-1][0]+1, H[-1][1]])
            elif move[0] == 'U':
                H.append([H[-1][0], H[-1][1]+1])
            elif move[0] == 'L':
                H.append([H[-1][0]-1, H[-1][1]])
            else:
                H.append([H[-1][0], H[-1][1]-1])
