# алгоритм пошуку в глибину
def dfs(graph, start, end, path=[]):
    loc_path = path + [start]
    if start == end:
        true_paths.append(loc_path)
    for node in graph[start]:
        if node not in loc_path:
            dfs(graph, node, end, loc_path)


P = [0.75, 0.1, 0.87, 0.55, 0.6, 0.28, 0.36, 0.76]
connections_graph = {0: [2, 3],
                     1: [2, 4],
                     2: [3, 4],
                     3: [5, 6],
                     4: [5, 7],
                     5: [6, 7],
                     6: [],
                     7: []}
connections_graph_size = len(connections_graph)
true_paths = []

dfs(connections_graph, 0, 6)
dfs(connections_graph, 0, 7)
dfs(connections_graph, 1, 6)
dfs(connections_graph, 1, 7)

# список всіх можливих шляхів
possible_paths = []
for i in range(2 ** connections_graph_size):
    var = []
    tmp = i
    for j in range(connections_graph_size, -1, -1):
        if tmp // (2 ** j) == 1:
            tmp = tmp % (2 ** j)
            var.append(j)
    possible_paths.append(sorted(var))

# список всіх працездатних шляхів
workable_paths = []
for i in possible_paths:
    for j in true_paths:
        if set(j).issubset(set(i)):
            workable_paths.append(i)
            break

# Ймовірність безвідмовної роботи системи
p_final = 0
for i in workable_paths:
    temp = 1
    for j in range(connections_graph_size):
        if int(j) in i:
            temp *= P[j]
        else:
            temp *= 1 - P[j]
    p_final += temp

print(f'Ймовірність безвідмовної роботи системи: {p_final}')
