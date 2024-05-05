import copy

stack = []
visited = []

def generatechildren(s):
    global stack
    global visited
    y = len(s)
    for i in range(y):
        temp = copy.deepcopy(s)
        if len(temp[i]) != 0:
            top_elem = temp[i][-1]
            del temp[i][-1]
            for j in range(y):
                if i != j:
                    new_state = copy.deepcopy(temp)
                    new_state[j].append(top_elem)
                    new_state[j].sort()
                    if new_state not in stack and new_state not in visited:
                        stack.append((new_state, 1))  # Push state and depth

def search(limit):
    global stack
    global visited
    while True:
        if len(stack) == 0:
            return False
        curr_state, depth = stack.pop()  # Unpack state and depth
        if depth > limit:
            continue
        if curr_state == g:
            print("Found")
            return True
        visited.append(curr_state)
        generatechildren(curr_state)

def main():
    global stack
    global visited
    global g
    s = [['A'], ['B', 'C'], []]
    g = [[], [], ['A', 'B', 'C']]
    stack.append((s, 0))  # Initialize stack with initial state and depth 0
    depth_limit = 1
    while True:
        if search(depth_limit):
            return
        depth_limit += 1
    print("Not Found")

if __name__ == "__main__":
    main()
