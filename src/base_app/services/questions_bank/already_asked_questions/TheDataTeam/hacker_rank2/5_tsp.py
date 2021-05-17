import copy


def min_cost(g_nodes, g_from, g_to, x, y, g_weight, visited, cost):

    if visited[x] is True and visited[y] is True and visited[g_to] is True:
        return cost


    for item in visited:
        for edge in g_weight:
            edge1 = edge[0]
            edge2 = edge[1]
            weight = edge[2]

            if visited[edge1] is not None and visited[edge2] is None:
                new_cost = copy.deepcopy()
                new_cost += weight
                visited[edge2] = True


def min_path_cost(g_nodes, g_from, g_to, g_weight, x, y):
    visited = dict()
    visited[g_from] = True
    cost = 0
    min_cost(g_nodes,g_from,g_to,g_weight,x, y, cost)



