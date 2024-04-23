def tree_by_levels(root):
    if not root:
        return []
    result = []
    q = [root]
    while q:
        node = q.pop(0)
        result.append(node.value)

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return result
