import sys
sys.setrecursionlimit(1500)

def dfs(Adj, s, parent = None, order = None):
    if parent is None:
        parent = [None for v in Adj]
        order = []
        parent[s] = s
    for v in Adj[s]:
        if parent[v] is None:
            parent[v] = s
            dfs(Adj, v, parent, order)
    order.append(s)
    return parent, order

def full_dfs(Adj):
    parent = [None for v in Adj]
    order = []
    for v in range(len(Adj)):
        if parent[v] is None:
            parent[v] = v
            dfs(Adj, v, parent, order)
    return parent, order
# above is given code from template file

# flip G to get revG and then run full_dfs on revG
# this gives a preceived meeting point, mp
# we then run a dfs on revG at the preceived mp to verify if that is indeed a true mp
# if it reaches all other nodes, then the size of that dfs list will be the total number of nodes present in G
def find_meeting_point(adj):

    revG = [[] for i in range(len(adj))]

    for i in range(len(adj)):
        for j in range(len(adj[i])):
            revG[adj[i][j]].append(i)

    (fullParent, fullOrder) = full_dfs(revG)
    mp = fullOrder[-1]

    (parent, order) = dfs(revG, mp)

    if len(revG) == len(order):

        return mp
