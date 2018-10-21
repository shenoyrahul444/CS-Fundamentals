from collections import deque
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        q = deque()
        visited = [0]*n
        for i,nodes in enumerate(graph):
            if nodes and visited[i] == 0:
                visited[i]=1
                q.appendleft(i)
                while q:
                    current = q.pop()
                    for nbr in graph[current]:
                        if visited[nbr] == 0:
                            visited[nbr] = 2 if visited[current]==1 else 1
                            q.appendleft(nbr)
                        elif visited[nbr] == visited[current]:
                            return False
                # stack = [i]
                # while stack:
                #     nxt = []
                #     for nd in stack:
                #         for nbr in graph[nd]:


        return True
graph = [[1,3],[0,2],[1,3],[0,2]]
print(Solution().isBipartite(graph))

