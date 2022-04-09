from math import log, factorial


# алгоритм пошуку в глибину
def dfs(graph, start, end, path=[]):
    loc_path = path + [start]
    if start == end:
        true_paths.append(loc_path)
    for node in graph[start]:
        if node not in loc_path:
            dfs(graph, node, end, loc_path)


P = [0.75, 0.1, 0.87, 0.55, 0.6, 0.28, 0.36, 0.76]
Q = [1 - p for p in P]
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
def find_p_system(paths_workable=[], p=[], graph_size=int):
    system_p = 0
    for i in paths_workable:
        temp = 1
        for j in range(graph_size):
            if int(j) in i:
                temp *= p[j]
            else:
                temp *= 1 - p[j]
        system_p += temp
    return system_p


p_system = find_p_system(workable_paths, P, connections_graph_size)

# Початок 3 ЛР
T = 2403
k_zag_nenav_rez = 1
k_rozd_nav_rez = 1
q_system = 1 - p_system
t_system = -T / log(p_system)
print(f'Ймовірність безвідмовної роботи системи без резервування: {p_system}')
print(f'Ймовірність відмови системи без резервування: {q_system}')
print(f'Середній наробіток до відмови системи без резервування: {t_system}\n')

q_reserved_system = (1 / factorial(k_zag_nenav_rez + 1)) * q_system
p_reserved_system = 1 - q_reserved_system
t_reserved_system = -T / log(p_reserved_system)
print(f'Ймовірність безвідмовної роботи системи з загальним ненавантаженим резервуванням: {p_reserved_system}')
print(f'Ймовірність відмови системи з загальним ненавантаженим резервуванням: {q_reserved_system}')
print(f'Середній наробіток до відмови системи з загальним ненавантаженим резервуванням: {t_reserved_system}\n')

g_q = q_reserved_system / q_system
g_p = p_reserved_system / p_system
g_t = t_reserved_system / t_system
print(f'Виграш надійності протягом часу {T} годин за ймовірністю відмов: {g_q}')
print(f'Виграш надійності протягом часу {T} годин за ймовірністю безвідмовної роботи: {g_p}')
print(f'Виграш надійності за середнім часом безвідмовної роботи: {g_t}\n')

Q_reserved = [q ** (k_rozd_nav_rez + 1) for q in Q]
P_reserved = [1 - q_res for q_res in Q_reserved]

P_reserved_system = find_p_system(workable_paths, P_reserved, connections_graph_size)
Q_reserved_system = 1 - P_reserved_system
T_reserved_system = -T / log(P_reserved_system)
print(f'Ймовірність безвідмовної роботи системи з роздільним навантаженим резервуванням: {P_reserved_system}')
print(f'Ймовірність відмови системи з роздільним навантаженим резервуванням: {Q_reserved_system}')
print(f'Середній наробіток до відмови системи з роздільним навантаженим резервуванням: {T_reserved_system}\n')

G_q = Q_reserved_system / q_system
G_p = P_reserved_system / p_system
G_t = T_reserved_system / t_system
print(f'Виграш надійності протягом часу {T} годин за ймовірністю відмов: {G_q}')
print(f'Виграш надійності протягом часу {T} годин за ймовірністю безвідмовної роботи: {G_p}')
print(f'Виграш надійності за середнім часом безвідмовної роботи: {G_t}\n')
