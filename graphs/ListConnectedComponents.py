'''
Given a graph/ Return a List with the number of nodes in each Connected Component
'''
def listConnectedComponents(n, edges):
    '''
    Approach: Easy variation of number of connected components
    TC: O(V+E)
    SC: O(V)
        if adjList is not given: O(V+E)
    '''
    adjList = [[] for _ in range(n)]

    for u,v in edges:
        adjList[u].append(v)
        adjList[v].append(u)
    
    ccli = []
    vis = [False]*n

    def dfs(node):
        vis[node] = True
        n_cc = 1
        for nei in adjList[node]:
            if not vis[nei]:
                n_cc += dfs(nei)
        return n_cc
    
    for i in range(n):
        if not vis[i]:
            ccli.append(dfs(i))
    
    return ccli

if __name__=="__main__":
    n = 10
    edges = [[0,1],[1,2],[3,4],[5,6],[7,8],[8,9]]
    print(listConnectedComponents(n, edges))