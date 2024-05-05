q = []

def compare(s, g):
    return s[1] == g[1]

def gen_child(curr_State):
    global s
    global q
    for i in range(len(s)):
        if curr_State[1] == s[i][0]:
            new_State = [curr_State[0] + s[i][2], s[i][1]]
#             print(new_State)
            found = False
            for j in range(len(q)):
                if new_State[1] == q[j][1]:
                    found = True
                    if new_State[0] < q[j][0]:
                        q[j][0] = new_State[0]
            if not found:
                q.append(new_State)
#             print(q)

def main():
    global s
    global q
    s = [['S', 'A', 1], ['S', 'B', 5], ['S', 'C', 15], ['A', 'G', 10], ['B', 'G', 5], ['C', 'G', 5]]
    g = [12343, 'G']
    q = [[0, 'S']]
    while q:
        curr_State = q.pop(0)
        if compare(curr_State, g):
            print("Goal reached with cost:", curr_State[0])
            return
        gen_child(curr_State)
    print("Goal not reachable")

main()