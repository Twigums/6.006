def find_start_times(constraints):
    # initialize the graph, distance dictionary, and V and E
    # the supernode is initialized since we don't see the supernode going through our constraints
    graph = {}
    dist = {}
    graph["supernode"] = {}
    dist["supernode"] = 0
    V = 1
    E = []

    # for each constraint, add an edge from the supernode to s_j if there is none already
    # add an edge from s_j -> s_i and add the weights accordingly
    # distances are initialized for all nodes to inf
    # for each s_j that is not in the dictionary, add 1 to V
    for (s_i, s_j, t_k) in constraints:
        if s_j not in graph:
            graph["supernode"][s_j] = 0
            E.append(("supernode", s_j))
            graph[s_j] = {}
            V += 1

        dist[s_i] = float("inf")
        dist[s_j] = float("inf")

        graph[s_j][s_i] = t_k
        E.append((s_j, s_i))

    # bellman ford as discussed in class
    for i in range(V - 1):
        for (v1, v2) in E:
            try_to_relax(graph, dist, v1, v2)

    for (v1, v2) in E:
        if dist[v2] > dist[v1] + graph[v1][v2]:
            return None

    return dist

# try to relax for bellman ford
# in this problem, we have no use for the parent, so no need to maintain that
def try_to_relax(graph, dist, a, v):
    if dist[v] > dist[a] + graph[a][v]:
        dist[v] = dist[a] + graph[a][v]
