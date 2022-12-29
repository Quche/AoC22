import math
import copy

rope_size = 10
nodes_xy = [[[0,0] for i in range(rope_size)]]

def adjacent(n1,n2):
    d = math.sqrt((n1[0]-n2[0])**2 + (n1[1]-n2[1])**2)
    if d <= math.sqrt(2):
        return True
    else:
        return False

def sameRowColumn(n1,n2):
    return (n1[0] == n2[0]) | (n1[1] == n2[1])

with open('inputs/day9/test2.txt') as f:

    for idx, line in enumerate(f.readlines()):

        move = line.rstrip().split(' ')
        nodes_tmp = copy.deepcopy(nodes_xy[-1])

        for inc in range(int(move[1])):

            # head
            init_state = copy.deepcopy(nodes_tmp)
            if move[0] == 'R':
                nodes_tmp[0][0] += 1
            elif move[0] == 'U':
                nodes_tmp[0][1] += 1
            elif move[0] == 'L':
                nodes_tmp[0][0] -= 1
            else:
                nodes_tmp[0][1] -= 1

            # other nodes
            for idx_node in range(1,rope_size):
                head = nodes_tmp[idx_node-1]
                tail = nodes_tmp[idx_node]
                if not adjacent(tail,head):
                    if sameRowColumn(tail,head):
                        nodes_tmp[idx_node] = init_state[idx_node-1]
                    else:
                        if (head[0] > tail[0]):
                            nodes_tmp[idx_node][0] += 1
                        if (head[1] > tail[1]):
                            nodes_tmp[idx_node][1] += 1
                        if (head[0] < tail[0]):
                            nodes_tmp[idx_node][0] -= 1
                        if (head[1] < tail[1]):
                            nodes_tmp[idx_node][1] -= 1

            nodes_xy.append(copy.deepcopy(nodes_tmp))

unique_el = []
for node in nodes_xy:
    if node[-1] not in unique_el:
        unique_el.append(node[-1])

print(f'Unique tail positions: {len(unique_el)}')



# beg = True
# for idx in range(len(H)-1):
#     cand = H[idx]
#     if dist(T[-1],H[idx+1]) > math.sqrt(2):
#         T.append(cand)

# print(f'Unique tail positions: {len(unique(T))}')

# for idx in range(len(H)-10):
#     cand = H[idx]
#     if dist(T[-1],H[idx+1]) > math.sqrt(2):
#         T.append(cand)