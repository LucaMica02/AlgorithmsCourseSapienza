'''
In a directed graph a well is a node with no outgoing edges
In a directed graph an universal well is a well to which all other nodes have an edge
The problem is to determine if a directed graph has an universal well
'''
def universalWellV1(matrix):

    #test if a node is an universal well
    def test(i, matrix):
        #check if from the node outgoing an edge
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                return False
        #check if exist a node which does not have an edge to the current node
        for j in range(len(matrix)):
            if j != i and matrix[j][i] == 0:
                return False
        return True

    #itering on the nodes and check if exist an universal well
    for i in range(len(matrix)):
        if test(i, matrix):
            return True
    return False
#Time complexity -> O(n*n) = O(n^2) 


def universalWellV2(matrix):

    #with a test i can delete a node from the possible universal wells
    #then n-1 tests will remain only a node to check
    L = [i for i in range(len(matrix))]
    while len(L) > 1:
        a = L.pop()
        b = L.pop()
        if matrix[a][b] == '1':
            L.append(b)
        else:
            L.append(a)
    node = L.pop()

    #check the last node
    for i in range(len(matrix)):
        if matrix[node][i] == '1':
            return False
    for i in range(len(matrix)):
        if i != node and matrix[i][node] == '0':
            return False
        
    return True
#Time complexity -> O(n + n + n + n) = O(4n) = O(n)


# Describe an algorithm that, given an undirected and connected graph G and 
# its two nodes u and v, finds the nodes that have the same distance from 
# u and v in O(n + m) time.
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

def solution(u, v, G):
    res = 0
    distU = BFSdistances(u,G)
    distV = BFSdistances(v,G)
    for i in range(len(G)):
        if distU[i] == distV[i]:
            res += 1
    return res


# Design an algorithm that, given a graph G, checks in O(n) time whether it is a tree or not.
# A tree is equivalent to an acyclic connected graph
def isTree(G):
    visited = [0] * len(G)

    def DFS(x, father, G, visited):
        visited[x] = 1
        for i in G[x]:
            if visited[i] == 1:
                if i != father:
                    return True
            else:
                if DFS(i, x, G, visited):
                    return True
        return False
    
    def BFS(node, G):
        v = [0] * len(G)
        v[node] = 1
        queue = [node]
        i = 0
        while len(queue) > i:
            u = queue[i]
            i += 1
            for n in G[u]:
                if v[n] == 0:
                    v[n] = 1
                    queue.append(n)
        return v
    
    for i in range(len(G)):
        if visited[i] == 0:
            if DFS(i, i, G, visited): return False

    for i in BFS(0, G):
        if i == 0: return False

    return True


'''
Given a graph of n nodes we have nodes that can be 'dangerous', we have 
a binary vector P that allows us to identify them where P[i] == 1 
if and only if the node is considered dangerous, the algorithm must 
return a vector of shortest paths where the cost of the path is given 
by the number of dangerous nodes we pass through to reach it.
'''
def solve(n, G, P):
    visited = [False]*len(G)
    res = [-1]*len(G)
    L = []
    sL = set()
    grade = 0

    def DFS(x,G,P,L,grade):
        visited[x] = True
        res[x] = grade
        for i in (G[x]):
            if not visited[i]:
                if P[i] != 1:
                    DFS(i,G,P,L,grade)
                else:
                    if i not in sL:
                        L.append(i)
                        sL.add(i)
    
    DFS(n,G,P,L,grade)
    while L:
        u = L.pop()
        sL.remove(u)
        grade += 1
        P[u] = 0
        DFS(u,G,P,L,grade)

    return res
# Time comlexity -> O(n+m)


""" 
Given a tree of n nodes represented by the parent vector P (by convention the parent of the root node is the node itself) 
and two tree nodes u and v, calculate the distance between u and v in the tree.
"""
def calcDistance(P, u, v):
    root = None
    dicU, dicV = dict(), dict()
    countU, countV = 0, 0
    flag = False
    for i in range(len(P)):
        if P[i] == i + 1:
            root = i + 1
            break
    while True:
        dicU[u] = countU
        countU += 1
        u = P[u - 1]
        if u == root:
            if not flag:
                flag = True
            else:
                break
    while True:
        if v in dicU:
            return dicU[v] + countV
        dicV[v] = countV
        countV += 1
        v = P[v - 1]
# Time comlexity -> O(n)
        

"""
Given a tree of n nodes represented by the parent vector P (for convention the parent of the root node is the node itself) 
and one of its nodes x, find the set of nodes of T present in the subtree rooted at x.
"""
def findSubtree(P, x):
    res = set()
    res.add(x)
    prev, curr = None, 1
    while prev != curr:
        for i in range(len(P)):
            if P[i] in res and i+1 not in res:
                res.add(i+1)
        prev = curr
        curr = len(res)
    return res


'''
The square graph of a directed graph G = (V,E) is a directed graph G2 = (V,E2)
where E2 = {(u, v) | ∃ w ∈ V and (u, w) ∈ E and (w, v) ∈ E}.
Describe an algorithm which, given the directed graph G, calculates the square graph G2
'''
def squareGraph(G):
    mapping = dict()
    for i in range(len(G)):
        mapping[i] = set(G[i])
        for j in G[i]:
            mapping[i].update(set(G[j]))
    for i in range(len(G)):
        G[i] = list(mapping[i])
    return G
# Time comlexity -> O((n+m)^2)


'''
Given a graph G, describe an algorithm that orients its edges so as 
to create a directed and acyclic G1 graph.
'''
def orientsGraph(G):
    newG = []
    for i in range(len(G)):
        L = []
        for j in G[i]:
            if j > i:
                L.append(j)
        newG.append(L)
    return newG
# Time comlexity -> O(n+m)


'''
A node n in a directed graph G, is principal if every other vertex in G
it can be reached with a direct path starting from n.
Given G and n return true if and only if n is a principal node.
'''
def pricipalNode(G, n):
    
    def DFS(G, n, V):
        V[n] = 1
        for i in G[n]:
            if V[i] == 0:
                DFS(G, i, V)

    V = [0] * len(G)
    DFS(G, n, V)
    if sum(V) == len(V):
        return True
    return False
# Time comlexity -> O(n+m)

''' Given G return true if and only if G contain a principal node. '''
def containPrincipalNode(G):

    def DFS(G, n, V):
        V[n] = 1
        for i in G[n]:
            if V[i] == 0:
                DFS(G, i, V)

    V = [0] * len(G)
    last = None
    # If the tree produced by a DFS on a node don't cover all the node in the graph
    # that node and all the nodes present in that tree aren't principal node
    for i in range(len(G)):
        if V[i] == 0:
            last = i
            DFS(G, i, V)
    # The last node that i called in the DFS maybe can be a principal node
    return pricipalNode(G, last)
# Time comlexity -> O(n+m)


'''
Given an undirected and connected graph G and two its
nodes u and v, find the nodes that have the same distance from u and v
'''
def sameDistance(G, u, v):
    
    def BFS(G, n):
        D = [float('inf')] * len(G) 
        D[n] = 0
        i = 0
        q = [n]
        while i < len(q):
            node = q[i]
            i += 1
            for j in G[node]:
                if D[j] == float('inf'):
                    q.append(j)
                    D[j] = D[node] + 1
        return D
    
    Du = BFS(G, u)
    Dv = BFS(G, v)
    res = set()
    for i in range(len(G)):
        if Du[i] == Dv[i]:
            res.add(i)
    return res
# Time comlexity -> O(n+m)


'''
Given a graph G and two subsets V1 and V2 of its nodes find their minimum distance, 
if the subsets are not disjoint returns 0
'''
def minDistSubset(G, V1, V2):
    D = [float('inf')] * len(G)
    q = []
    i = 0
    for v1 in V1:
        D[v1] = 0
        q.append(v1)
    while i < len(q):
        node = q[i]
        if node in V2:
            return D[node]
        for j in G[node]:
            if D[j] == float('inf'):
                D[j] = D[node] + 1
                q.append(j)
    return float('inf')
# Time comlexity -> O(n+m)


'''
Given a graph G, a node n, a distance vector related to a BFS from n and
an edge (u,v) of G, returns true if and only if removing the edge 
(u,v) does not change the distances from n
'''
def removeEdge(G, D, n, edge):
    u, v = edge
    G[u].remove(v)
    G[v].remove(u)

    def BFS(G, n):
        D = [float('inf')] * len(G) 
        D[n] = 0
        i = 0
        q = [n]
        while i < len(q):
            node = q[i]
            i += 1
            for j in G[node]:
                if D[j] == float('inf'):
                    q.append(j)
                    D[j] = D[node] + 1
        return D
    
    D1 = BFS(G, n)
    if D1 == D:
        return True
    return False