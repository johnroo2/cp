from typing import Optional


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        stack = [node]
        visited = set()
        edges = set()
        node_map = {}

        while stack:
            current = stack.pop()

            if current in visited:
                continue

            visited.add(current)
            
            if current.val not in node_map:
                node_map[current.val] = Node(current.val)

            for neighbor in current.neighbors:
                edges.add((min(current.val, neighbor.val), max(current.val, neighbor.val)))
                stack.append(neighbor)
        
        for edge in edges:
            node_map[edge[0]].neighbors.append(node_map[edge[1]])
            node_map[edge[1]].neighbors.append(node_map[edge[0]])
        
        return node_map[1]
