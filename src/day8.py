def day8_1(grid):
    grid_len = len(grid)
    grid_width = len(grid[0])
    n_edges = 2*grid_len + 2*(grid_width - 2)
    c = 0

    for i in range(1,grid_len - 1):
        for j in range(1,grid_width -1):

            size = int(grid[i][j])

            ts = [int(grid[t][j]) for t in range(0,i)]
            ls = [int(grid[i][t]) for t in range(0,j)]
            bs = [int(grid[t][j]) for t in range(i+1,grid_width)]
            rs = [int(grid[i][t]) for t in range(j+1,grid_len)]

            for l in [ts,ls,bs,rs]:
                if all([size > el for el in l]):
                    c += 1
                    break


    print(f'Total trees visible from outside: {c+n_edges}')

def day8_2(grid):

    grid_len = len(grid)
    grid_width = len(grid[0])
    max_scenir_score = 0
    inc = 0
    for i in range(1,grid_len - 1):
        for j in range(1,grid_width - 1):
            inc += 1
            size = int(grid[i][j])

            ts = [int(grid[t][j]) for t in range(0,i)][::-1]
            ls = [int(grid[i][t]) for t in range(0,j)][::-1]
            bs = [int(grid[t][j]) for t in range(i+1,grid_width)]
            rs = [int(grid[i][t]) for t in range(j+1,grid_len)]

            scenic_score = 1
            for l in [ts,ls,bs,rs]:
                compare = [size > el for el in l]
                if False in compare:
                    scenic_score *= compare.index(False) + 1
                else:
                    scenic_score *= len(compare)

            if scenic_score > max_scenir_score:
                max_scenir_score = scenic_score

    print(f'Max scenic score: {max_scenir_score}')

grid = []
with open('inputs/day8/day8.txt') as f:
    for line in f.readlines():
        line = line.rstrip()
        grid.append([line[i] for i in range(len(line))])

day8_1(grid)
day8_2(grid)