# ── Trees ────────────────────────────────────────────────────────────────────
# Binary Tree | Binary Search Tree (BST) | AVL Tree

# ─── Binary Tree Node ────────────────────────────────────────────────────────

class TreeNode:
    def __init__(self, data):
        self.data  = data
        self.left  = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.data})"


class BST:
    def __init__(self):
        self.root = None

    # ── insert ───────────────────────────────────────────────────────────────

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return TreeNode(data)
        if data < node.data:
            node.left  = self._insert(node.left,  data)
        elif data > node.data:
            node.right = self._insert(node.right, data)
        return node 

    def search(self, data):
        """Return True if data exists in the tree."""
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        return(self._search(node.left, data) 
            if data < node.data \
            else self._search(node.right, data))

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return None
        if data < node.data:
            node.left  = self._delete(node.left,  data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            # Found the node to delete
            if node.left is None:   
                return node.right
            if node.right is None:  
                return node.left
            # Two children: replace with in-order successor (min of right subtree)
            successor = self._min_node(node.right)
            node.data  = successor.data
            node.right = self._delete(node.right, successor.data)
        return node

    def _min_node(self, node):
        while node.left:
            node = node.left
        return node

    def inorder(self):
        """L -> Root -> R"""
        traversal = []
        self._inorder(self.root, traversal)
        return traversal

    def _inorder(self, node, traversal):
        if node:
            self._inorder(node.left,  traversal)
            traversal.append(node.data)
            self._inorder(node.right, traversal)

    def preorder(self):
        """Root -> Left -> Right"""
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(node.data)
            self._preorder(node.left,  result)
            self._preorder(node.right, result)

    def postorder(self):
        """Left -> Right -> Root"""
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left,  result)
            self._postorder(node.right, result)
            result.append(node.data)

    def level_order(self):
        """BFS level by level using a queue."""
        if not self.root:
            return []
        result, queue = [], [self.root]
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        return result

    # ── properties ───────────────────────────────────────────────────────────

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1   # height of empty tree = -1
        return 1 + max(self._height(node.left), self._height(node.right))

    def count_nodes(self):
        return self._count(self.root)

    def _count(self, node):
        if node is None:
            return 0
        return 1 + self._count(node.left) + self._count(node.right)

    def is_valid_bst(self):
        """Verify BST property holds for the whole tree."""
        return self._is_valid(self.root, float('-inf'), float('inf'))

    def _is_valid(self, node, min_val, max_val):
        if node is None:
            return True
        if not (min_val < node.data < max_val):
            return False
        return (self._is_valid(node.left,  min_val,    node.data) and
                self._is_valid(node.right, node.data,  max_val))

    def min_value(self):
        if not self.root: return None
        return self._min_node(self.root).data

    def max_value(self):
        node = self.root
        while node.right:
            node = node.right
        return node.data

    def __repr__(self):
        return f"BST(inorder={self.inorder()})"

    # ── Visual Representation ────────────────────────────────────────────────
    
    def __str__(self):
        if self.root is None:
            return "Empty BST"
        return self._build_tree_str(self.root, "", True, "Root: ")

    def _build_tree_str(self, node, prefix="", is_last=True, branch_label=""):
        if node is None:
            return ""
        
        # Build the string for the current node
        result = prefix
        if prefix:
            result += "└── " if is_last else "├── "
            
        result += f"{branch_label}{node.data}\n"
        
        # Calculate the prefix for the children
        child_prefix = prefix + ("    " if is_last else "│   ")
        
        # Recursively build left and right children
        if node.left and not node.right:
            # Only has a left child, so it's technically the "last" printed item for this node
            result += self._build_tree_str(node.left, child_prefix, True, "L: ")
        elif node.left and node.right:
            # Has both. Left is printed first (not last), Right is printed second (is last).
            result += self._build_tree_str(node.left, child_prefix, False, "L: ")
            result += self._build_tree_str(node.right, child_prefix, True, "R: ")
        elif node.right:
            # Only has right child
            result += self._build_tree_str(node.right, child_prefix, True, "R: ")
            
        return result


# ── Testing the BST ──────────────────────────────────────────────────────────

bst = BST()
for v in [5, 6, 16, 62, 61, 65, 51, 7, 9, 11]:
    bst.insert(v)

print(bst) # This automatically calls the new __str__ method
print("The BST inorder traversal:   " + str(bst.inorder()))
print("The BST postorder traversal: " + str(bst.postorder()))
print("The BST preorder traversal:  " + str(bst.preorder()))