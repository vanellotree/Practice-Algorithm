# 미루고 미루던 다익스트라 드디어 했다 !
# 예전엔 뭔지 감도 안 왔었는데, 어느 순간 조금 이해하게 되었고,
# 지금도 갈길이 멀었지만 그래도 예전에 못 풀었던 이 문제를 비교적 수월하게 해결한
# 내 스스로를 보면서 미세하게 3초 뿌듯했다 (과거-형) 앞으로도 파팅 > <

import sys
import heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dijkstra(start):
    global dist

    queue = []
    heapq.heappush(queue, (0, start))
    dist[start] = 0

    while queue:
        cur_dist, cur_node = heapq.heappop(queue)
        if dist[cur_node] < cur_dist:
            continue
        for next_node, weight in graph[cur_node]:
            cost = cur_dist + weight
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(queue, (cost, next_node))


vertex, edge = map(int, input().split())
k = int(input())
graph = [[] for _ in range(vertex + 1)]
INF = int(1e9)
dist = [INF for _ in range(vertex + 1)]

for _ in range(edge):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(k)

for i in range(1, vertex + 1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
