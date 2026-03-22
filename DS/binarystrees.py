# ── Binary Search Tree (BST) ──────────────────────────────────────────────────


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

    # ── insert ────────────────────────────────────────────────────────────────

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

    # ── search ────────────────────────────────────────────────────────────────

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        return (self._search(node.left,  data)
                if data < node.data
                else self._search(node.right, data))

    # ── delete ────────────────────────────────────────────────────────────────

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
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            successor  = self._min_node(node.right)
            node.data  = successor.data
            node.right = self._delete(node.right, successor.data)
        return node

    def _min_node(self, node):
        while node.left:
            node = node.left
        return node


    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left,  result)
            result.append(node.data)
            self._inorder(node.right, result)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(node.data)
            self._preorder(node.left,  result)
            self._preorder(node.right, result)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left,  result)
            self._postorder(node.right, result)
            result.append(node.data)

    def level_order(self):
        if not self.root:
            return []
        result, queue = [], [self.root]
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        return result


    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    def count_nodes(self):
        return self._count(self.root)

    def _count(self, node):
        if node is None:
            return 0
        return 1 + self._count(node.left) + self._count(node.right)

    def is_valid_bst(self):
        return self._is_valid(self.root, float('-inf'), float('inf'))

    def _is_valid(self, node, min_val, max_val):
        if node is None:
            return True
        if not (min_val < node.data < max_val):
            return False
        return (self._is_valid(node.left,  min_val,   node.data) and
                self._is_valid(node.right, node.data, max_val))

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

    # ── visual representation ─────────────────────────────────────────────────

    def __str__(self):
        if self.root is None:
            return "Empty BST"
        return self._build_tree_str(self.root, "", True, "Root: ")

    def _build_tree_str(self, node, prefix="", is_last=True, branch_label=""):
        if node is None:
            return ""
        result = prefix
        if prefix:
            result += "└── " if is_last else "├── "
        result += f"{branch_label}{node.data}\n"
        child_prefix = prefix + ("    " if is_last else "│   ")
        if node.left and node.right:
            result += self._build_tree_str(node.left,  child_prefix, False, "L: ")
            result += self._build_tree_str(node.right, child_prefix, True,  "R: ")
        elif node.left:
            result += self._build_tree_str(node.left,  child_prefix, True,  "L: ")
        elif node.right:
            result += self._build_tree_str(node.right, child_prefix, True,  "R: ")
        return result



def menu():
    print("\n\t\t----------------------------------------")
    print("\n\t\t1. Insert a Node")
    print("\n\t\t2. Search for a Node")
    print("\n\t\t3. Delete a Node")
    print("\n\t\t4. Traverse the BST")
    print("\n\t\t5. Tree Properties")
    print("\n\t\t6. Quit")
    print("\n\t\t----------------------------------------")
    print("\n\t\tYour choice please: ", end="")


def traverse_menu(bst):
    print("\n\t\t  --- Traversal Options ---")
    print("\n\t\t  a. Inorder   (L -> Root -> R)")
    print("\n\t\t  b. Preorder  (Root -> L -> R)")
    print("\n\t\t  c. Postorder (L -> R -> Root)")
    print("\n\t\t  d. Level Order (BFS)")
    print("\n\t\t  e. Visual Tree")
    print("\n\t\t  Choice: ", end="")
    sub = input().strip().lower()

    if sub == 'a':
        print(f"\n\t\tInorder   : {bst.inorder()}")
    elif sub == 'b':
        print(f"\n\t\tPreorder  : {bst.preorder()}")
    elif sub == 'c':
        print(f"\n\t\tPostorder : {bst.postorder()}")
    elif sub == 'd':
        print(f"\n\t\tLevel Order: {bst.level_order()}")
    elif sub == 'e':
        print(f"\n{bst}")
    else:
        print("\n\t\tInvalid sub-option!")


def properties_menu(bst):
    print("\n\t\t  --- Tree Properties ---")
    print("\n\t\t  a. Height")
    print("\n\t\t  b. Node Count")
    print("\n\t\t  c. Min Value")
    print("\n\t\t  d. Max Value")
    print("\n\t\t  e. Check Valid BST")
    print("\n\t\t  Choice: ", end="")
    sub = input().strip().lower()

    if sub == 'a':
        print(f"\n\t\tHeight     : {bst.height()}")
    elif sub == 'b':
        print(f"\n\t\tNode Count : {bst.count_nodes()}")
    elif sub == 'c':
        print(f"\n\t\tMin Value  : {bst.min_value()}")
    elif sub == 'd':
        print(f"\n\t\tMax Value  : {bst.max_value()}")
    elif sub == 'e':
        valid = bst.is_valid_bst()
        print(f"\n\t\tValid BST? : {'Yes' if valid else 'No'}")
    else:
        print("\n\t\tInvalid sub-option!")


def main():
    bst = BST()

    while True:
        menu()
        try:
            choice = int(input().strip())
        except ValueError:
            print("\n\t\tWrong input! Please enter 1-6.")
            continue

        if choice == 1:
            print("\n\t\tEnter value to insert: ", end="")
            try:
                value = int(input().strip())
                if bst.search(value):
                    print(f"\n\t\t{value} already exists in the BST!")
                else:
                    bst.insert(value)
                    print(f"\n\t\t{value} was inserted into the BST!")
            except ValueError:
                print("\n\t\tInvalid value! Please enter an integer.")

        elif choice == 2:
            print("\n\t\tEnter value to search: ", end="")
            try:
                value = int(input().strip())
                if bst.search(value):
                    print(f"\n\t\t{value} was FOUND in the BST!")
                else:
                    print(f"\n\t\t{value} was NOT FOUND in the BST!")
            except ValueError:
                print("\n\t\tInvalid value! Please enter an integer.")

        elif choice == 3:
            print("\n\t\tEnter value to delete: ", end="")
            try:
                value = int(input().strip())
                if not bst.search(value):
                    print(f"\n\t\t{value} was NOT FOUND in the BST!")
                else:
                    bst.delete(value)
                    print(f"\n\t\t{value} was deleted from the BST!")
            except ValueError:
                print("\n\t\tInvalid value! Please enter an integer.")

        elif choice == 4:
            if bst.root is None:
                print("\n\t\tBST is EMPTY!")
            else:
                traverse_menu(bst)

        elif choice == 5:
            if bst.root is None:
                print("\n\t\tBST is EMPTY!")
            else:
                properties_menu(bst)

        elif choice == 6:
            print("\n\t\tYou decided to QUIT\n\n\t\tBYE!\n")
            break

        else:
            print("\n\t\tWrong input! Please enter 1-6.")


main()