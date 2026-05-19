# Problem 133: Clone Graph

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        
        visited = {}
        
        def dfs(node):
            if node in visited:
                return visited[node]
            
            copy = Node(node.val)
            visited[node] = copy
            
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        
        return dfs(node)