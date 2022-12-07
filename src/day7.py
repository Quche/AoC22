def day7_path_storage(path):

    dirs = dict({'/':0})
    current_path = ''

    with open(path) as f:

            i = 0
            for line in f.readlines():
                i += 1
                if i == 1:
                    continue

                line_el = line.rsplit()

                if line_el[0] == '$': # command
                    if line_el[1] == 'cd':
                        if line_el[2] == '..':
                            current_path = '/'.join(current_path.split('/')[:-1])
                        else:
                            current_path = '/'.join([current_path,line_el[2]])

                elif (line_el[0] == 'dir'): # directory
                    path_to_create = '/'.join([current_path,line_el[1]])
                    if path_to_create not in dirs.keys():
                        dirs[path_to_create] = 0

                else: # files
                    file_size = int(line_el[0])
                    dirs['/'] += file_size
                    path_folders_list = current_path.split('/')
                    if current_path != '':
                        for i in range(2,len(path_folders_list) + 1):
                            key = '/'.join(path_folders_list[:i])
                            dirs[key] += file_size

    return dirs

def day7_1(dirs, limit_size):

    s = 0
    for d in dirs.keys():
        if dirs[d] <= limit_size:
            s += dirs[d]
    print(f'Total size of directories under {limit_size}: {s}')

def day7_2(dirs, space_needed, total_space):

    to_empty = space_needed - (total_space - dirs['/'])
    min_empty = dirs['/']
    for k in dirs.keys():
        vol = to_empty - dirs[k]
        if vol < 0 and dirs[k] < min_empty:
            min_empty = dirs[k]
    print(f'The size of the dir to empty is: {min_empty}')


dirs = day7_path_storage('inputs/day7/day7.txt')
day7_1(dirs, 100000)
day7_2(dirs, 30000000, 70000000)
