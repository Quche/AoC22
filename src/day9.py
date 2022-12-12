H = [[0,0]]
S = [0,0]
T = [S]
i = 0

def unique(my_list):
    unique_el = []
    for l in my_list:
        if l not in unique_el:
            unique_el.append(l)
    return unique_el


with open('inputs/day9/test.txt') as f:
    i += 1
    for line in f.readlines():

        move = line.rstrip().split(' ')
        for inc in range(int(move[1])):

            # Head
            if move[0] == 'R':
                newH = H[-1]
                H.append([H[-1][0]+1, H[-1][1]])
            elif move[0] == 'U':
                H.append([H[-1][0], H[-1][1]+1])
            elif move[0] == 'L':
                H.append([H[-1][0]-1, H[-1][1]])
            else:
                H.append([H[-1][0], H[-1][1]-1])

            # Tail
            if (H[-2][1] != H[-1][1]) & (H[-2][0] != H[-1][0]):
                pass
            else:
                T.append(H[-1])

            print(H[-1],T[-1])

unique_T = unique(T)
print(f'Total number of distinct position of tail: {unique_T}')
