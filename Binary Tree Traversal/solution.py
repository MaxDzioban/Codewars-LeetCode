# Pre-order traversal
def pre_order(node):
    if node is None:
        return []
    talon = [node.data]
    talon += pre_order(node.left)
    talon += pre_order(node.right)
    return talon

# In-order traversal
def in_order(node):
    if node is None:
        return []
    talon = []
    talon += in_order(node.left)
    talon.append(node.data)
    talon += in_order(node.right)
    return talon

def post_order(node):
    if node is None:
        return []
    talon = []
    talon += post_order(node.left)
    talon += post_order(node.right)
    talon.append(node.data)
    return talon

