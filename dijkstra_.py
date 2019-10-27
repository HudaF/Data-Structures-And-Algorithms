def getShortestPath(G, s, d):
    Q = initialize(G.keys(),s)
    W = initialize(G.keys(),s)
    p={s:None}
    path = []
    while Q:
        u = extract_min(Q)
        for v,w in G[u]:
            Relax(W,u,v,w,p)
##    print(p) #complete path dict
    
    while d !=None: #going from d to s in path (ulta)
        path.append(d) 
        d = p[d]
    path.reverse() #it was ulta so making it seedha
    return path
        
def initialize(V,s):
    Q = {}
    for vertex in V:
        Q[vertex] = float("inf")
    Q[s] = 0
    return Q

def extract_min(Q):
    v = min(Q,key = Q.get)
    Q.pop(v)
    return v

def Relax(W,u,v,w,p): 
    new_weight = W[u] + w #if prims instead of dijkstra we only do  new_weight = W[u]
    if new_weight < W[v]:
        W[v] = new_weight
        p[v] = u
        
def addNodes(G,nodes):
    for i in nodes:
        G[i]=[]
    return G

def addEdges(G,edges,directed):
    if directed == False:
        for i in edges:
            if len(i)==3:
                G[i[0]].append(i[1:])
                G[i[1]].append((i[0],i[2]))
            else:
                G[i[0]].append((i[1],1))
                G[i[1]].append((i[0],1))
        return G
    else:
        for i in edges:
            if len(i)==3:
                G[i[0]].append((i[1:]))
            else:
                G[i[0]].append((i[1],1))
        return G
G={}
addNodes(G,['A','B','C','D','E','F','G'])
edges=[('A', 'B', 7), ('A', 'E', 6), ('A', 'D', 2), ('B', 'C', 3), ('C', 'D', 2), ('C', 'G', 2), ('D', 'F', 8), ('E', 'F', 9), ('F', 'G', 4)]
addEdges(G,edges,False)
print(G)
print('\n')
print(getShortestPath(G, 'A', 'G'))
    
    
