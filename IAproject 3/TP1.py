import argparse
import sys
import timeit
import resource
from collections import deque
from state import State
from heapq import heappush, heappop, heapify
import itertools
algorithm=""
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
goal_node = State
initial_state = list()
board_len = 0
board_side = 0

nodes_expanded = 0
max_search_depth = 0
max_frontier_size = 0

moves = list()
costs = set()
def rebegin():
    global moves,costs,nodes_expanded,max_search_depth,max_frontier_size,goal_node
    goal_node = State
    nodes_expanded = 0
    max_search_depth = 0
    max_frontier_size = 0
    moves = list()
    costs = set()

def bfs(start_state):

    global max_frontier_size, goal_node, max_search_depth

    explored, queue = set(), deque([State(start_state, None, None, 0, 0, 0)])

    while queue:

        node = queue.popleft()

        explored.add(node.map)
        
        if node.state == goal_state:
            goal_node = node
            return queue

        neighbors = expand(node)

        for neighbor in neighbors:
            if neighbor.map not in explored:
                queue.append(neighbor)
                explored.add(neighbor.map)

                if neighbor.depth > max_search_depth:
                    max_search_depth += 1

        if len(queue) > max_frontier_size:
            max_frontier_size = len(queue)

def costfunction(e):
    return e.cost



def ucs(start_state):

    global max_frontier_size, goal_node, max_search_depth

    explored, heap = set(), list()
    root=State(start_state, None, None, 0, 0, 0)
    entry=(root.cost,root)
    heappush(heap,entry)

    while heap:

        node = heappop(heap)

        explored.add(node[1].map)
        
        if node[1].state == goal_state:
            goal_node = node[1]
            return heap

        neighbors = expand(node[1])

        for neighbor in neighbors:
            if neighbor.map not in explored:
                newentry=(neighbor.cost,neighbor)
                heappush(heap,newentry)
                explored.add(neighbor.map)

                if neighbor.depth > max_search_depth:
                    max_search_depth += 1

        if len(heap) > max_frontier_size:
            max_frontier_size = len(heap)


def ida(start_state):

    global costs

    threshold = 0

    while 1:
        response = dls_mod(start_state, threshold)

        if type(response) is list:
            return response
            break

        threshold +=1




def dls_mod(start_state, threshold):

    global max_frontier_size, goal_node, max_search_depth, costs

    explored, stack = set(), list([State(start_state, None, None, 0, 0, threshold)])

    while stack:

        node = stack.pop()

        explored.add(node.map)

        if node.state == goal_state:
            goal_node = node
            return stack

        if node.depth < threshold:


            neighbors = reversed(expand(node))

            for neighbor in neighbors:
                if neighbor.map not in explored:
                    stack.append(neighbor)
                    explored.add(neighbor.map)

                    if neighbor.depth > max_search_depth:
                        max_search_depth += 1

            if len(stack) > max_frontier_size:
                max_frontier_size = len(stack)

    return False


def dfs(start_state):

    global max_frontier_size, goal_node, max_search_depth

    explored, stack = set(), list([State(start_state, None, None, 0, 0, 0)])

    while stack:

        node = stack.pop()

        explored.add(node.map)

        if node.state == goal_state:
            goal_node = node
            return stack

        neighbors = reversed(expand(node))

        for neighbor in neighbors:
            if neighbor.map not in explored:
                stack.append(neighbor)
                explored.add(neighbor.map)

                if neighbor.depth > max_search_depth:
                    max_search_depth += 1

        if len(stack) > max_frontier_size:
            max_frontier_size = len(stack)


def ast1(start_state):
    global max_frontier_size, goal_node, max_search_depth
    explored, heap, heap_entry, counter = set(), list(), {}, itertools.count()

    key = h1(start_state)

    root = State(start_state, None, None, 0, 0, key)

    entry = (key, 0, root)

    heappush(heap, entry)

    heap_entry[root.map] = entry

    while heap:

        node = heappop(heap)

        explored.add(node[2].map)

        if node[2].state == goal_state:
            goal_node = node[2]
            return heap

        neighbors = expand(node[2])

        for neighbor in neighbors:

            neighbor.key = neighbor.cost + h1(neighbor.state)

            entry = (neighbor.key, neighbor.move, neighbor)

            if neighbor.map not in explored:

                heappush(heap, entry)

                explored.add(neighbor.map)

                heap_entry[neighbor.map] = entry

                if neighbor.depth > max_search_depth:
                    max_search_depth += 1

            elif neighbor.map in heap_entry and neighbor.key < heap_entry[neighbor.map][2].key:

                hindex = heap.index((heap_entry[neighbor.map][2].key,
                                     heap_entry[neighbor.map][2].move,
                                     heap_entry[neighbor.map][2]))

                heap[int(hindex)] = entry

                heap_entry[neighbor.map] = entry

                heapify(heap)

        if len(heap) > max_frontier_size:
            max_frontier_size = len(heap)


def gbfs1(start_state):
    global max_frontier_size, goal_node, max_search_depth
    explored, heap, heap_entry, counter = set(), list(), {}, itertools.count()

    key = h1(start_state)

    root = State(start_state, None, None, 0, 0, key)

    entry = (key, 0, root)

    heappush(heap, entry)

    heap_entry[root.map] = entry

    while heap:

        node = heappop(heap)

        explored.add(node[2].map)

        if node[2].state == goal_state:
            goal_node = node[2]
            return heap

        neighbors = expand(node[2])

        for neighbor in neighbors:

            neighbor.key =  h1(neighbor.state)

            entry = (neighbor.key, neighbor.move, neighbor)

            if neighbor.map not in explored:

                heappush(heap, entry)

                explored.add(neighbor.map)

                heap_entry[neighbor.map] = entry

                if neighbor.depth > max_search_depth:
                    max_search_depth += 1

            elif neighbor.map in heap_entry and neighbor.key < heap_entry[neighbor.map][2].key:

                hindex = heap.index((heap_entry[neighbor.map][2].key,
                                     heap_entry[neighbor.map][2].move,
                                     heap_entry[neighbor.map][2]))

                heap[int(hindex)] = entry

                heap_entry[neighbor.map] = entry

                heapify(heap)

        if len(heap) > max_frontier_size:
            max_frontier_size = len(heap)

def ast2(start_state):
    global max_frontier_size, goal_node, max_search_depth
    explored, heap, heap_entry, counter = set(), list(), {}, itertools.count()

    key = h2(start_state)

    root = State(start_state, None, None, 0, 0, key)

    entry = (key, 0, root)

    heappush(heap, entry)

    heap_entry[root.map] = entry

    while heap:

        node = heappop(heap)

        explored.add(node[2].map)

        if node[2].state == goal_state:
            goal_node = node[2]
            return heap

        neighbors = expand(node[2])

        for neighbor in neighbors:

            neighbor.key = neighbor.cost + h2(neighbor.state)

            entry = (neighbor.key, neighbor.move, neighbor)

            if neighbor.map not in explored:

                heappush(heap, entry)

                explored.add(neighbor.map)

                heap_entry[neighbor.map] = entry

                if neighbor.depth > max_search_depth:
                    max_search_depth += 1

            elif neighbor.map in heap_entry and neighbor.key < heap_entry[neighbor.map][2].key:

                hindex = heap.index((heap_entry[neighbor.map][2].key,
                                     heap_entry[neighbor.map][2].move,
                                     heap_entry[neighbor.map][2]))

                heap[int(hindex)] = entry

                heap_entry[neighbor.map] = entry

                heapify(heap)

        if len(heap) > max_frontier_size:
            max_frontier_size = len(heap)


def gbfs2(start_state):
    global max_frontier_size, goal_node, max_search_depth
    explored, heap, heap_entry, counter = set(), list(), {}, itertools.count()

    key = h2(start_state)

    root = State(start_state, None, None, 0, 0, key)

    entry = (key, 0, root)

    heappush(heap, entry)

    heap_entry[root.map] = entry

    while heap:

        node = heappop(heap)

        explored.add(node[2].map)

        if node[2].state == goal_state:
            goal_node = node[2]
            return heap

        neighbors = expand(node[2])

        for neighbor in neighbors:

            neighbor.key =  h2(neighbor.state)

            entry = (neighbor.key, neighbor.move, neighbor)

            if neighbor.map not in explored:

                heappush(heap, entry)

                explored.add(neighbor.map)

                heap_entry[neighbor.map] = entry

                if neighbor.depth > max_search_depth:
                    max_search_depth += 1

            elif neighbor.map in heap_entry and neighbor.key < heap_entry[neighbor.map][2].key:

                hindex = heap.index((heap_entry[neighbor.map][2].key,
                                     heap_entry[neighbor.map][2].move,
                                     heap_entry[neighbor.map][2]))

                heap[int(hindex)] = entry

                heap_entry[neighbor.map] = entry

                heapify(heap)

        if len(heap) > max_frontier_size:
            max_frontier_size = len(heap)


def keyfunction(e):
    return e.key


def HC(start_state):
    global max_frontier_size, goal_node, max_search_depth
    initial_key=h2(start_state)
    node= State(start_state, None, None, 0, 0, initial_key)
    count=0
    while count<10:
        if node.state == goal_state:
            goal_node = node
            return []
        neighbors = expand(node)
        neighbors.sort(reverse=True,key=keyfunction)
        if node.key==neighbors[0].key:
            count+=1
            previous_node=node
        else:
            count=0
        node=neighbors[0]
    goal_node=node
    return[]

def expand(node):

    global nodes_expanded
    nodes_expanded += 1

    neighbors = list()

    neighbors.append(State(move(node.state, 1), node, 1, node.depth + 1, node.cost + 1, 0))
    neighbors.append(State(move(node.state, 2), node, 2, node.depth + 1, node.cost + 1, 0))
    neighbors.append(State(move(node.state, 3), node, 3, node.depth + 1, node.cost + 1, 0))
    neighbors.append(State(move(node.state, 4), node, 4, node.depth + 1, node.cost + 1, 0))

    nodes = [neighbor for neighbor in neighbors if neighbor.state]

    return nodes


def move(state, position):

    new_state = state[:]

    index = new_state.index(0)
    if position == 1:  # Up

        if index not in range(0, board_side):

            temp = new_state[index - board_side]
            new_state[index - board_side] = new_state[index]
            new_state[index] = temp

            return new_state
        else:
            return None

    if position == 2:  # Down

        if index not in range(board_len - board_side, board_len):

            temp = new_state[index + board_side]
            new_state[index + board_side] = new_state[index]
            new_state[index] = temp

            return new_state
        else:
            return None

    if position == 3:  # Left

        if index not in range(0, board_len, board_side):

            temp = new_state[index - 1]
            new_state[index - 1] = new_state[index]
            new_state[index] = temp

            return new_state
        else:
            return None

    if position == 4:  # Right

        if index not in range(board_side - 1, board_len, board_side):

            temp = new_state[index + 1]
            new_state[index + 1] = new_state[index]
            new_state[index] = temp

            return new_state
        else:
            return None

def h2(state):
    return sum(abs(b % board_side - g % board_side) + abs(b//board_side - g//board_side)
               for b, g in ((state.index(i), goal_state.index(i)) for i in range(1, board_len)))
def h1(state):
    count=0
    if state[0]!=1:
       count=count+1
    if state[1]!=2:
       count=count+1
    if state[2]!=3:
       count=count+1
    if state[3]!=4:
       count=count+1
    if state[4]!=5:
       count=count+1
    if state[5]!=6:
       count=count+1
    if state[6]!=7:
       count=count+1
    if state[7]!=8:
       count=count+1
    return count

def backtrace():

    current_node = goal_node
    
    
    while initial_state != current_node.state:
        # print("olha o g",g(current_node.state))
        # print(current_node.state[0:3])
        # print(current_node.state[3:6])
        # print(current_node.state[6:9])
        # print("\n")
        if current_node.move == 1:
            movement = 'Up'
        elif current_node.move == 2:
            movement = 'Down'
        elif current_node.move == 3:
            movement = 'Left'
        else:
            movement = 'Right'

        moves.insert(0, movement)
        current_node = current_node.parent

    return moves

def myprint(mymovement):
    mystate=initial_state
    for n in mymovement:
        indexzero= mystate.index(0)
        print(mystate[0:3])
        print(mystate[3:6])
        print(mystate[6:9])
        print("\n")
        if n=='Up':
            indexmovement=indexzero-3
            mystate[indexzero]=mystate[indexmovement]
            mystate[indexmovement]=0
        if n=='Down':
            indexmovement=indexzero+3
            mystate[indexzero]=mystate[indexmovement]
            mystate[indexmovement]=0
        if n=='Left':
            indexmovement=indexzero-1
            mystate[indexzero]=mystate[indexmovement]
            mystate[indexmovement]=0
        if n=='Right':
            indexmovement=indexzero+1
            mystate[indexzero]=mystate[indexmovement]
            mystate[indexmovement]=0
    print(mystate[0:3])
    print(mystate[3:6])
    print(mystate[6:9])


def export(frontier, time,print_me):
    global moves
    moves = backtrace()
    if print_me:
        myprint(moves)
    file = open(algorithm+'calma.txt', 'w')
    file.write("\npath_to_goal: " + str(moves))
    file.write("\ncost_of_path: " + str(len(moves)))
    file.write("\nnodes_expanded: " + str(nodes_expanded))
    file.write("\nfringe_size: " + str(len(frontier)))
    file.write("\nmax_fringe_size: " + str(max_frontier_size))
    file.write("\nsearch_depth: " + str(goal_node.depth))
    file.write("\nmax_search_depth: " + str(max_search_depth))
    file.write("\nrunning_time: " + format(time, '.8f'))
    file.write("\nmax_ram_usage: " + format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1000.0, '.8f'))    
    file.close()
def h1export(frontier, time):
    global moves
    moves = backtrace()
    file = open(algorithm+'calma.txt', 'w')
    file.write("\nHeuristica relaxada demais")
    file.write("\npath_to_goal: " + str(moves))
    file.write("\ncost_of_path: " + str(len(moves)))
    file.write("\nnodes_expanded: " + str(nodes_expanded))
    file.write("\nfringe_size: " + str(len(frontier)))
    file.write("\nmax_fringe_size: " + str(max_frontier_size))
    file.write("\nsearch_depth: " + str(goal_node.depth))
    file.write("\nmax_search_depth: " + str(max_search_depth))
    file.write("\nrunning_time: " + format(time, '.8f'))
    file.write("\nmax_ram_usage: " + format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1000.0, '.8f'))
    return file
def h2export(frontier, time, file, print_me):
    global moves
    moves = backtrace()
    if print_me:
        myprint(moves)
    file.write("\nHeuristica mais proxima do custo real")
    file.write("\npath_to_goal: " + str(moves))
    file.write("\ncost_of_path: " + str(len(moves)))
    file.write("\nnodes_expanded: " + str(nodes_expanded))
    file.write("\nfringe_size: " + str(len(frontier)))
    file.write("\nmax_fringe_size: " + str(max_frontier_size))
    file.write("\nsearch_depth: " + str(goal_node.depth))
    file.write("\nmax_search_depth: " + str(max_search_depth))
    file.write("\nrunning_time: " + format(time, '.8f'))
    file.write("\nmax_ram_usage: " + format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1000.0, '.8f'))    
    file.close()
def read(configuration):

    global board_len, board_side,initial_state

    data = configuration

    for element in data:
        initial_state.append(int(element))

    board_len = len(initial_state)

    board_side = int(board_len ** 0.5)


def main():
    global algorithm
    mylist=sys.argv
    algorithm= str(mylist[1])
    
    rest= mylist[2:]
    
    if rest[-1]=='PRINT':
        printe=True
        rest=rest[0:9]
    else:
        printe=False
    rest=[int(x) for x in rest]

    read(rest)
    if algorithm=='A' or algorithm=='G':
        function1, function2 = alt_function_map[algorithm]
        start=timeit.default_timer()
        frontier=function1(initial_state)
        stop=timeit.default_timer()
        file=h1export(frontier,stop-start)
        rebegin()
        start=timeit.default_timer()
        frontier=function2(initial_state)
        stop=timeit.default_timer()
        h2export(frontier,stop-start,file,printe)
    else:
        function = function_map[algorithm]
        start = timeit.default_timer()
        frontier = function(initial_state)
        stop = timeit.default_timer()
        export(frontier, stop-start,printe)

alt_function_map = {
    'A': (ast1,ast2),
    'G': (gbfs1,gbfs2)
}

function_map = {
    'B': bfs,
    'D': dfs,
    'I': ida,
    'U':ucs,
    'H':HC

}

if __name__ == '__main__':
    main()