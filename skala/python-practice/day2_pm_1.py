# -------------------------------------------------------------
# 작성자 : 
# 작성목적 : KDT 교육용 비선형 자료구조 (DFS & BFS 탐색)
# 작성일 : 2025-02-20
# 본 파일은 KDT 교육을 위한 Sample 코드이므로 작성자에게 모든 저작권이 있습니다.
# 
# 변경사항 내역 (날짜, 변경목적, 변경내용 순으로 기입)
# 
# -------------------------------------------------------------

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph[node])

    return result

print("BFS 탐색 결과:", bfs(graph, 'A'))

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))

    return result

print("DFS 탐색 결과:", dfs(graph, 'A'))
