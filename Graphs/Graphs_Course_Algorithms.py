# Visit the nodes of graph reachable from u in O(n+m)
def reachableNodes(u, G):
    def DFS(u, G, visit):
        visit[u] = 1
        for i in G[u]:
            if visit[i] == 0:
                DFS(i, G, visit)
    visit = [0]*len(G)
    DFS(u, G, visit)
    return visit
# Time Complexity -> O(n+m)


# Generates the vector of the parents, i.e. a vector of n components
# of a graph seen as a tree where i is a node and P[i] contains the
# father of node i, i same if i is root or -1 if i is not in the tree
def reachableNodes(u, G):
    def DFS(u, G, P):
        for i in G[u]:
            if P[i] == -1:
                P[i] = u
                DFS(i, G, P)
    P = [-1]*len(G)
    P[u] = u
    DFS(u, G, P)
    return P
# Time Complexity -> O(n+m)


# Return the path from the root of P to the node u
def path(u, P):
    if P[u] == -1:
        return []
    res = []
    while P[u] != u:
        res.append(u)
        u = P[u]
    res.append(u)
    res.reverse()
    return res
# Time Complexity -> O(n)


# Given a connected graph we want to know if it is possible to color 
# the nodes of the graph in two distinct colors so that adjacent 
# nodes always have distinct colors.
def twoTone(G):

    def DFS(x, G, colors, c):
        colors[x] = c
        for i in G[x]:
            if colors[i] ==  -1:
                if not DFS(i, G, colors, -c):
                    return False
            elif colors[i] == c:
                return False
        return True
    
    color = [-1]*len(G)
    if DFS(0, G, color, 0):
        return color
    return []
# returns a bicolor if the graph is bicolor an empty list otherwise
# Time Complexity -> O(n+m)


# A connected component of an (indirect) graph is a subgraph composed of a maximal set of nodes connected by paths.
# The algorithm returns the vector C of the connected components of the graph G
def connectedComponents(G):
    def DFS(i, G, C, counter):
        C[i] = counter
        for j in G[i]:
            if C[j] == 0:
                DFS(j, G, C, counter)

    C = [0]*len(G)
    counter = 0
    for i in range(len(G)):
        if C[i] == 0:
            counter += 1
            DFS(i, G, C, counter)
    return C
# Time Complexity -> O(n+m)


# G1 transpose of a graph G is a graph with the same nodes, but with the edges in the opposite direction
# Given a graph G this algorithm returns the transpose G1
def transpose(G):
    G1 = [[] for _ in G]
    for i in range(len(G)):
        for j in G[i]:
            G1[j].append(i)
    return G1
# Time Complexity -> O(n+m)


# returns a topological sort of G if exists an empty list otherwise
def TPsort(G):
    grades = [0] * len(G)
    for i in range(len(G)):
        for j in G[i]:
            grades[j] += 1
    sources = [i for i in range(len(G)) if grades[i] == 0]
    TS = []
    while len(sources) > 0:
        node = sources.pop()
        TS.append(node)
        for i in G[node]:
            grades[i] -= 1
            if grades[i] == 0:
                sources.append(i)
    if len(TS) == len(G):
        return TS
    return []
# Time Complexity -> O(n+m)


# other implementaion of topological sort based on DFS
def TPsort(G):
    def DFS(node,G,visited,res):
        visited[node] = 1
        for i in G[node]:
            if visited[i] == 0:
                DFS(i,G,visited,res)
        res.append(node)

    visited = [0] * len(G)
    res = []
    for i in range(len(G)):
        if visited[i] == 0:
            DFS(i,G,visited,res)
    res.reverse()
    return res
# Time Complexity -> O(n+m)


# given a node and a graph i want to know if from node i can reach a cycle in G
# directed graph
def cycleDG(u, G):
    visited = [0]*len(G)
    
    def DFS(u, father, G, visited):
        visited[u] = 1
        for i in G[u]:
            if (visited[i] == 1 and i != father) or DFS(i, u, G, visited):
                return True
        return False

    return DFS(u, u, G, visited)
# Time Complexity -> O(n+m)

# undirected graph
def cycleUG(u, G):
    visited = [0]*len(G)
    
    def DFS(u, G, visited):
        visited[u] = 1
        for i in G[u]:
            if visited[i] == 1 or (visited[i] == 0 and DFS(i, G, visited)):
                return True
        visited[u] = 2
        return False

    return DFS(u, G, visited)
# Time Complexity -> O(n+m)


# A bridge is an edge whose elimination disconnects the graph
def findBridges(G):
    height = [-1]*len(G)
    bridges = []

    def DFS(node, h, G, height, bridges):
        height[node] = h
        ret = float('inf')
        for i in G[node]:
            if height[i] == -1:
                k = DFS(i, h+1, G, height, bridges)
                if h < k:
                    bridges.append((node,i))
                ret =  min(ret, k)
            elif height[i] != h-1:
                ret =  min(ret, height[i])
        return ret

    DFS(0, 0, G, height, bridges)
    return bridges
# Time Complexity -> O(n+m)


# Given a node and a graph return the BFS visit
def BFS(node, G):
    visited = [0] * len(G)
    visited[node] = 1
    queue = [node]
    i = 0
    while len(queue) > i:
        u = queue[i]
        i += 1
        for n in G[u]:
            if visited[n] == 0:
                visited[n] = 1
                queue.append(n)
    return visited
# Time Complexity -> O(n+m)
            

# Given a node and a graph return the vector of the fathers of the BFS visit
def BFSfathers(node, G):
    fathers = [-1] * len(G)
    fathers[node] = node
    queue = [node]
    i = 0
    while len(queue) > i:
        u = queue[i]
        i += 1
        for n in G[u]:
            if fathers[n] == -1:
                fathers[n] = u
                queue.append(n)
    return fathers
# Time Complexity -> O(n+m)


# Given a node and a graph return the vector of the minimum distances from node to the other nodes of G
def BFSdistances(node, G):
    distances = [-1] * len(G)
    distances[node] = 0
    queue = [node]
    i = 0
    while len(queue) > i:
        u = queue[i]
        i += 1
        for n in G[u]:
            if distances[n] == -1:
                distances[n] = distances[u] + 1
                queue.append(n)
    return distances
# Time Complexity -> O(n+m)


# Returns the distance vector and the shortest path tree via vector of 
# the parents of a weighted graph starting from a node
def dijkstraDenseGraphs(node, G):
    visited = [False] * len(G)
    distances = [float('inf')] * len(G)
    parents = [-1] * len(G)
    distances[node], parents[node], visited[node] = 0, node, True
    for i, cost in G[node]:
        distances[i], parents[i] = cost, node
    while True:
        minimum = float('inf')
        for i in range(len(G)):
            if not visited[i] and distances[i] < minimum:
                minimum, n = distances[i], i
        if minimum == float('inf'):
            break
        visited[n] = True
        for j, cost in G[n]:
            if not visited[j] and minimum + cost < distances[j]:
                distances[j], parents[j] = minimum + cost, n
    return distances, parents
# Time complexity -> O(n^2)


def dijkstraSparseGraph(node, G):
    from heapq import heappop, heappush
    distances = [float('inf')] * len(G)
    parents = [-1] * len(G)
    distances[node], parents[node] = 0, node
    heap = []
    for i, cost in G[node]:
        heappush(heap, (cost, node, i))
    while heap:
        cost, father, n = heappop(heap)
        if parents[n] == -1:
            parents[n] = father
            distances[n] = cost
            for j, cost1 in G[n]:
                heappush(heap, (distances[n] + cost1, n, j))
    return distances, parents
# Time complexity -> O((n+m) * logn)


# Algorithm for computing the minimum spanning trees of an undirected, connected, weighted graph.
def kruskal(G):

    def create(G):
        return [(i,1) for i in range(len(G))]

    def union(a, b, C):
        totA, totB = C[a][1], C[b][1]
        if totA >= totB:
            C[a] = (a, totA + totB)
            C[b] = (a, totB)
        else:
            C[b] = (b, totA + totB)
            C[b] = (a, totB)

    def find(x, C):
        while x != C[x][0]:
            x = C[x][0]
        return x

    tree = [[] for _ in G]
    edges = [(cost, x ,y) for x in range(len(G)) for y, cost in G[x] if x < y]
    edges.sort(reverse=True)
    C = create(tree)

    while edges:
        cost, x, y = edges.pop()
        cx = find(x, C)
        cy = find(y, C)
        if cx != cy:
            tree[x].append(y)
            tree[y].append(x)
            union(cx, cy, C)

    return tree
# Time complexity -> O(m*lgn)