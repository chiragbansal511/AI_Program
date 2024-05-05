import copy

q = []
visited = []

def generatechildren(s):
    global q
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
                    if new_state not in q and new_state not in visited:
                        q.append(new_state)

def search():
    global q
    global visited
    while True:
        curr_state = q[0]
        del q[0]
        if curr_state == g:
            print("found")
            exit()
        visited.append(curr_state)
        generatechildren(curr_state)

def main():
    global q
    global visited
    global g
    s = [['A'], ['B', 'C'], []]
    g = [[], [], ['A', 'B', 'C']]
    q.append(s)
    search()

if __name__ == "__main__":
    main()
