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
                        stack.append(new_state)

def search():
    global stack
    global visited
    while True:
        if len(stack) == 0:
            return False
        curr_state = stack.pop()
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
    stack.append(s)
    if not search():
        print("Not Found")

if __name__ == "__main__":
    main()
