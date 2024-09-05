import sys
sys.setrecursionlimit(10000)
#nodes = []
graph = []

# while True:
#     temp = int(sys.stdin.readline())
#     if temp == 0:
#         break
#     nodes.append(temp)

nodes = [int(line.strip()) for line in sys.stdin.readlines()]

#print(nodes)

def make_tree(start, end):
    if end - start == 0:
        graph.append([start, False, False])
        return
    elif end - start == 1:
        if nodes[start] < nodes[end]:
            graph.append([end, False, False])
            graph.append([start, False, end])
            return
        else:
            graph.append([end, False, False])
            graph.append([start, end, False])
            return

    left_end = end + 1

    for i in range(start + 1, end + 1):
        if nodes[start] < nodes[i]:
            left_end = i - 1
            break


    if left_end == start:
        left = False
        right = left_end + 1
        make_tree(right, end)
    elif left_end == end + 1:
        left = start + 1
        right = False
        make_tree(left, end)
    else:
        left = start + 1
        right = left_end + 1
        make_tree(left, left_end)
        make_tree(right, end)

    graph.append([start, left, right])

make_tree(0, len(nodes) - 1)

#print(graph)

for i in graph:
    print(nodes[i[0]])