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

def listOfNodes(G):
    return [i for i in G.keys()]

def listOfEdges(G,directed):
        edg = []
        for i in G:
            edg.append(G[i])
        return edg


def printInDegreeOutDegree(G):
    lst_edges=listOfEdges(G,False)
    lst_nodes=listOfNodes(G)
    Out={}
    In={}
    for i in range(len(lst_nodes)):
        Out[lst_nodes[i]]=len(lst_edges[i]) #out-degree is len(value) of key in Graph
        In[lst_nodes[i]] = sum(lst_edges[j].count(lst_nodes[i]) for j in range (len(lst_edges)))
    return In,Out

def getNeighbors(G,node):
    return G[node]

def getNearestNeighbor(G,node):
    neighbours = getNeighbors(G,node)
    sorted_neigh = sorted(neighbours, key=lambda x: x[1])
    return sorted_neigh[0][0]

def mutualneighbor(G,node1,node2):
    if node2 in  G[node1]: #G[noed] is neighbour
        return True
    return False

def removeNodes(G,node):
    if node in G:
        del G[node]
    for i in G.values():
        for j in i:
            if j[0]==node:
                i.remove(j)
    return G

def displayGraph(G):
    return G

def display_adj_matrix(G):
    matrix = [[0 for i in range(len(G))] for i in range(len(G))] #null 2d array
    for i in sorted(listOfNodes(G)):
        for j in getNeighbors(G,i):
            matrix[sorted(listOfNodes(G)).index(i)][sorted(listOfNodes(G)).index(j[0])]=1
    return matrix

G={}
nodes=[1,2,3,4,5]
edges=[(1,5,3),(1,2,6),(2,5,4),(5,4,9),(4,2,6),(3,4,7),(3,2)]

print('addNodes: ',(addNodes(G,nodes)))
print('addEdges: ',(addEdges(G,edges,False)))
print('list of Nodes  ',(listOfNodes(G)))
print('list of edges  ',listOfEdges(G,False))
print(printInDegreeOutDegree(G))
print('Removed updated graph', removeNodes(G,5))
print(display_adj_matrix(G))