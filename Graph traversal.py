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
addNodes(G,[0,1,2,3,4,5])
G = addEdges(G,[(0,1),(0,2),(1,3),(1,2),(2,4),(3,5),(3,4),(4,5)],True)
print(G)
print('\n')


def DFS_visit(G,s,parent):
    for u,v in G[s]:
        if u not in parent:
            parent[u]=s
            DFS_visit(G,u,parent)
    return parent

def DFS(G,parent):
    for i in G:
        if i not in parent:
            DFS_visit(G,i,parent)
            parent[i]=None
    return parent


def BFS(G,s):
    parent={s:None}
    frontier=[s]
    while frontier:
        next_lst=[]
        for i in frontier:
            for u,v in G[i]:
                if u not in parent:
                    parent[u]=i
                    next_lst.append(u)
        frontier=next_lst
    return parent

print(BFS(G,0))

print(DFS(G,{}))
