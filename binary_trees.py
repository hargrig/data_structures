from collections import deque


class Node:
    def __init__(self, key):
        self.data = key
        self.left, self.right = None, None


# Helper functions ----------------------------------------------------------------------

def height(node: Node) -> int:
    """ Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
    
    Parameters
    ----------
    node: Node

    Returns
    -------
        int

    """
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)
 
        # Use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1

# ---------------------------------------------------------------------------------------


# 1. Level Order
def level_order(root):
    for i in range(1, height(root)+1): 
        print(f"Level{i}"), print_curr_lvl(root, i)

def print_curr_lvl(root: Node, level: int):
    """ Prints current levels nodes

    Parameters
    ----------
    root: Node
    level: int

    """
    if root is None: return

    if level == 1: print(root.data)
    elif level > 1:
        level-=1
        print_curr_lvl(root.left, level), print_curr_lvl(root.right, level)


# 2. Level Order Using Queue
def print_level_order(root):

    # Base Case
    if not root: return

    q = deque()
     
    # Enqueue root and initialize height
    q.append(root)

    while True:
        # nodeCount (queue size) indicates
        # number of nodes at current level
        node_count = len(q)
        if node_count == 0: break
 
        # Dequeue all nodes of current level and Enqueue all nodes of next level
        while node_count > 0:
            node = q.popleft()

            print(node.data)

            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

            node_count -= 1

        print()


# 3. Inorder
def inorder(root: Node):
    """ Inorder traversal of tree LRR (Left Root Right)

    Parameters
    ----------
    root: Node 

    """
    if root is None: return

    inorder(root.left), print(root.data), inorder(root.right)


# 4. Preorder
def preorder(root: Node):
    """ Preorder traversal of tree RLR (Root Left Right)

    Parameters
    ----------
    root: Node 

    """
    if root is None: return

    print(root.data), preorder(root.left), preorder(root.right)


# 5. Postorder
def postorder(root: Node):
    """ Postorder traversal of tree RLR (Left Right, Root)

    Parameters
    ----------
    root: Node 

    """
    if root is None: return

    postorder(root.left), postorder(root.right), print(root.data)


# 6. Check if tree is a SUMTREE
def sum_tree(root: Node) -> int:
    """ Returns all nodes datas' sum
    
    Parameters
    ----------
    root: Node

    """
    if not root: 
        return 0
    else:
        return root.data + sum_tree(root.left) + sum_tree(root.right)

def is_sum_tree(root: Node) -> bool:
    """ Check if all root nodes equal to child nodes' data sums

    Parameters
    ----------
    root: Node

    """
    if not root or (not root.left and not root.right):
        return True

    ls, rs = sum_tree(root.left), sum_tree(root.right)

    if (root.data == ls + rs) and is_sum_tree(root.left) and is_sum_tree(root.right):
        return True

    return False


# 7. Check if tree is SIMETRIC
def is_simetric(root1: Node, root2: Node) -> bool:

    if not root1 and not root2:
        return True

    if root1 and root2 and (root1.data == root2.data):
        return (
            is_simetric(root1.left, root2.right) and 
            is_simetric(root1.right, root2.left)
        )

    return False


# 8
def preorder_return(root: Node):
    """ Preorder traversal of tree RLR (Root Left Right)

    Parameters
    ----------
    root: Node 

    """
    if not root: return []
    else: return [
        root.data, *preorder_return(root.left), *preorder_return(root.right)

    ]


# 9. Check if 2 trees are identical
def are_identical(root1: Node, root2: Node) -> bool:
    """ Check if 2 trees are identical

    Parameters
    ----------
    root1: Node
    root2: Node

    """
    if not root1 and not root2:
        return True

    if root1 and root2 and root1.data == root2.data:
        return(
            are_identical(root1.left, root2.left) and \
            are_identical(root1.right, root2.right)
        )

    return False


# 10. Flep the binary tree
def flip_tree(root: Node) -> Node:
    """ Flips the tree

    Parameters
    ----------
    root: Node

    """
    if not root: return root
    if not root.left and not root.right: return root

    flipped = flip_tree(root.left)

    root.left.left = root.right
    root.left.right = root

    root.left = root.right = None

    return flipped


# 11. Invert the tree
def invert_tree(root: Node) -> Node:

    if not root.left and not root.right:
        return root

    curr = root.left
    root.left = root.right
    root.right = curr

    invert_tree(root.left), invert_tree(root.right)

    return root


# 12. If tree contains the value
def contains_value(node: Node, value: int) -> bool:
    """

    """
    if not node: return False
    if node.data == value: return True

    return contains_value(node.left, value) or contains_value(node.right, value)


if __name__ == "__main__":
 
    # Driver program to test above function
    # root = Node(26)

    # root.left= Node(10)
    # root.right = Node(3)
    # root.left.left = Node(4)
    # root.left.right = Node(6)
    # root.right.right = Node(3)

    # print("Level order traversal")
    # level_order(root)
    # print()

    # print("Inorder traversal")
    # preorder(root)
    # print()

    # print("Preorder traversal")
    # preorder(root)
    # print()

    # print("Postorder traversal")
    # postorder(root)
    # print()

    # print("Is tree SUM_OF_TREE")
    # print(is_sum_tree(root))
    # print()

    # root1 = Node(1)
    # root1.left = Node(2)
    # root1.right = Node(2)
    # root1.left.left = Node(3)
    # root1.left.right = Node(4)
    # root1.right.left = Node(4)
    # root1.right.right = Node(3)

    # root1.left.right.left = Node(2)
    # root1.right.left.left = Node(2)

    # print("Is tree SIMETRIC")
    # print(is_simetric(root1.left, root1.right))
    # print()

    # f_root = Node(1)
    # f_root.left = Node(2)
    # f_root.right = Node(3)
    # f_root.left.left = Node(4)
    # f_root.left.right = Node(5)

    # s_root = Node(1)
    # s_root.left = Node(2)
    # s_root.right = Node(3)
    # s_root.left.left = Node(4)
    # s_root.left.right = Node(5)

    # print("Are 2 trees identical")
    # print(are_identical(f_root, s_root))
    # print(are_identical(f_root, None))
    # print()

    _root = Node(1)
    _root.left = Node(2)
    _root.right = Node(3)
    _root.right.left = Node(4)
    _root.right.right = Node(5)

    # print("Flip the tree")
    # print_level_order(_root)
    # flipped = flip_tree(_root)
    # print()
    # print_level_order(flipped)
    # print()

    # print("Invert the tree")
    # print_level_order(_root)
    # print()
    # inverted_tree = invert_tree(_root)
    # print_level_order(
    #     inverted_tree
    # )

    # print(inverted_tree.data)

    print("Contains the value")
    print(contains_value(_root, ))
