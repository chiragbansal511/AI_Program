import copy
import math
import random

q = []
visited = []

def generateChildren(s):
    global q
    global visited
    for i in range(len(s)):
        newState = copy.deepcopy(s)
        if newState[i] == 0:
            newState[i] = 1
        else:
            newState[i] = 0
        if newState not in q and newState not in visited:
            q.append(newState)

def heuristic(s):
    exp = [(not s[0]) or s[3], s[2] or s[1], (not s[2]) or (not s[3]), (not s[3]) or (not s[1]), (not s[0]) or (not s[3])]
    return sum(exp)

def calc(s, nextNode,T):
    global q
    global visited

    if heuristic(s) == 5:
        print("Found")
        return [s, T]
    
    if len(q) == 0: 
        generateChildren(s)

    if T == 0 or len(q) == 0:
        print("Optimal Not Found")
        print("Best Possible")
        return [s, T]
    
    nextNode = q[0]
    del(q[0])
    visited.append(nextNode)

    delta_E = heuristic(nextNode) - heuristic(s)
    p = 1 / (1 + math.exp(-delta_E/T))
    r = random.random()
    
    if r <= p:
        s = nextNode
        q.clear()
    T -= 10
    return calc(s, nextNode, T)


def search(s, exp):
    global q
    T = 1000
    if heuristic(s) == 5:
        print("Found")
        exit
    generateChildren(s)
    visited.append(s)
    nextNode = q[0]
    [s, T] = calc(s, nextNode, T)
    print(s)
    print("At Iteration: ", (1000-T)/10)
    

def main():
    s = [0, 0, 0, 0]
    exp = [(not s[0]) or s[3], s[2] or s[1], (not s[2]) or (not s[3]), (not s[3]) or (not s[1]), (not s[0]) or (not s[3])]
    search(s, exp)


if __name__ == "__main__":
    main()