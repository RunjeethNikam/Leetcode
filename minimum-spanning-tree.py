from collections import defaultdict
from heapq import *


def find_parent(u, parent):
    if parent[u] == u:
        return u
    else:
        parent[u] = find_parent(parent[u], parent)
        return parent[u]


def merge_unions(u, v, parent, rank):
    pu = find_parent(u, parent)
    pv = find_parent(v, parent)
    if rank[pu] == rank[pv]:
        parent[pu] = pv
        rank[pv] += 1
    elif rank[pu] < rank[pv]:
        parent[pu] = pv
    else:
        parent[pv] = pu


N, M = map(int, input().split())
edges = []
for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append([u, v, w])

parent = list(range(N + 1))
rank = [0] * (N + 1)

edges.sort(key=lambda edge: edge[-1])  # NlogN
nodes = 0
wt = 0
for u, v, w in edges:
    pu = find_parent(u, parent)
    pv = find_parent(v, parent)
    if pu == pv:
        pass
    else:
        nodes += 1
        wt += w
        merge_unions(pu, pv, parent, rank)

print(wt)


# # Prims Algorithm
# N, M = map(int, input().split())
# edges = defaultdict(list)

# for _ in range(M):
#     u, v, w = map(int, input().split())
#     edges[u].append({"node": v, "weight": w})
#     edges[v].append({"node": u, "weight": w})

# wt = 0

# key = [(0, 1)]  # Finding the next neightbor
# mst = [False] * (N + 1)  # tracking nodes in MST
# # parent = [-1] * (N + 1)  # for recreating the MST

# while key:
#     mn, u = heappop(key)
#     if mst[u]:
#         continue
#     wt += mn

#     mst[u] = True
#     for adj in edges[u]:
#         # parent[adj["node"]] = u
#         if not mst[adj["node"]]:
#             heappush(key, (adj["weight"], adj["node"]))
# print(wt)
