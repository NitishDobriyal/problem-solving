from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.horizontal_distance = 0  # Horizontal distance from the root

def top_view(root):
    if root is None:
        return []

    # Initialize a queue for level order traversal
    queue = deque([(root, 0)])  # Queue stores nodes along with their horizontal distances
    top_view_map = {}  # Map to store the top view nodes
    
    # Perform level order traversal
    while queue:
        node, hd = queue.popleft()
        
        # If horizontal distance is not in the map, add the node to the map
        if hd not in top_view_map:
            top_view_map[hd] = node.val
            
        # Update horizontal distance for child nodes and add them to the queue
        if node.left:
            node.left.horizontal_distance = hd - 1
            queue.append((node.left, hd - 1))
        if node.right:
            node.right.horizontal_distance = hd + 1
            queue.append((node.right, hd + 1))
    
    # Extract the top view nodes from the map and return them
    return [top_view_map[hd] for hd in sorted(top_view_map.keys())]

# Example usage:
# Construct a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)

# Find the top view of the binary tree
top_view_nodes = top_view(root)
print("Top view of the binary tree:", top_view_nodes)
