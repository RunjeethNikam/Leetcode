from collections import defaultdict

N = int(input())
Q = int(input())
graph = defaultdict(set)
# ancestor = defaultdict(set)

for _ in range(N-1):
    U, V = map(int, input().split())
    graph[U].add(V)
    graph[V].add(U)

visited = [False for _ in range(N+1)]
def dfs(parent):
    if not visited[parent]:
        visited[parent] = True
        for ng in graph[parent]:
            if visited[ng]:
                graph[parent] = graph[parent].union(graph[ng])
            dfs(ng)
dfs(1)
print(graph)

for _ in range(Q):
    X, Y = map(int, input().split())
    # print("YES" if X in ancestor[Y] else "NO")