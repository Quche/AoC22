import csv

def day1_1():

    with open('inputs/day1/day1.txt') as f:
        i = 0
        E = 0
        max_energy = 0
        max_elf = 0
        while True:
            line = f.readline()
            if line == '\n':
                if E > max_energy:
                    max_energy = E
                    max_elf = i
                print(f'Elfe {i}: {E}')
                i += 1
                E = 0
            elif not line:
                energy.append(E)
                print(f'Elfe {i}: {E}')
                print('End of file')
                break
            else:
                E = E + int(line.rstrip())

    print(f'Max elf: {max_elf} with {max_energy} energy.')

def day1_2():

    with open('inputs/day1/day1.txt') as f:
        E = 0
        E1, E2, E3 = 0, 0, 0
        while True:
            line = f.readline()
            if line == '\n':
                if E > E1:
                    E1 = E
                elif E > E2:
                    E2 = E
                elif E > E3:
                    E3 = E
                E = 0
            elif not line:
                print('End of file')
                break
            else:
                E = E + int(line.rstrip())

    print(f'Max 3e lfs with {E1 + E2 + E3} energy.')