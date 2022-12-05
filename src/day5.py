def temp_day5(crane_type):

    stacks_dict = dict()
    stacks = []
    orders = []
    isorder = False

    with open('inputs/day5/day5.txt') as f:

        for line in f.readlines():
            if line.rstrip() == '':
                isorder = True
                continue
            if not isorder:
                stacks.append(line.rstrip())
            else:
                orders.append(line.rstrip())

    # Parse initial stack to dictionnary
    stack_nb = [int(stacks[-1][i]) for i in range(1,len(stacks[-1]),4)]
    for nb in stack_nb:
        stacks_dict[nb] = []
    for layer in stacks[:-1][::-1]:
        el = [layer[i] for i in range(1,len(layer),4)]
        for i, e in enumerate(el):
            if e != ' ':
                stacks_dict[i+1] += e

    # parse orders
    orders = [orders[i].replace('move ','').replace(' from ','-').replace(' to ','-').split('-') for i in range(len(orders))]

    # Execute operations:
    for order in orders:

        qty = int(order[0])
        source = int(order[1])
        target = int(order[2])

        load = stacks_dict[source][-qty:]
        stacks_dict[source] = stacks_dict[source][:-qty]
        if crane_type == '9000':
            stacks_dict[target] += load[::-1]
        elif crane_type == '9001':
            stacks_dict[target] += load

    # Message
    message = ''
    for stack in stack_nb:
        message += stacks_dict[stack][-1]

    print(f'the message is: {message}')

def day5_1():
    temp_day5('9000')

def day5_2():
    temp_day5('9001')

day5_1()
day5_2()