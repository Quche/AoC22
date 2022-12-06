
repet = 14

def temp_day6(repet):

    with open('inputs/day6/day6.txt') as f:
        line = f.readline()

    i = 0
    while True:

        str_list = line[i: repet+i]
        if len(set(str_list)) == repet:
            print(f'Marker detected after: {repet+i}')
            break
        else:
            i += 1

def day6_1():
    repet = 4
    temp_day6(repet)

def day6_2():
    repet = 14
    temp_day6(repet)

day6_1()
day6_2()

