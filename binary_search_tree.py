class Node:
    def __init__(self, key: int):
        self.data = key
        self.left, self.right = None, None

def min_value_node(node):
    current = node
 
    # loop down to find the leftmost leaf
    while(current.left is not None):
        current = current.left
 
    return current

def inorder(root: Node):
    if root:
        inorder(root.left), print(root.data), inorder(root.right)


# 1. Check the value to be inserted (say X) with the value of the 
#    current node (say val) we are in:
#      1.1 If X is less than val move to the left subtree.
#      1.2 Otherwise, move to the right subtree.
# 2. Once the leaf node is reached, insert X to its right or left based on the 
#    relation between X and the leaf node’s value.
def insert(root: Node, key: int):
    """ Insert new key into binary search tree

    Parameters
    ----------
    root: Node
    key: int

    """
    if root is None: return Node(key)
    else:
        if root.data == key: return root
        elif root.data < key: root.right = insert(root.right, key)
        else: root.left = insert(root.left, key)

    return root


# 1. If the root is NULL, then return root (Base case)
# 2. If the key is less than the root’s value,
#    then set root->left = deleteNode(root->left, key)
# 3. If the key is greater than the root’s value, 
#    then set root->right = deleteNode(root->right, key)
# 4. Else check
#       4.1 If the root is a leaf node then return null
#       4.2 else if it has only the left child, then return the left child
#       4.3 else if it has only the right child, then return the right child
#       4.4 else set the value of root as of its inorder successor and 
#           recur to delete the node with the value of the inorder successor
# 5. Return
def delete(root: Node, key: int):
    """ Delete the key from binary search tree

    Parameters
    ----------
    root: Node
    key: int

    """
    if not root: return root

    # If the key to be deleted is smaller than the root's
    # key then it lies in  left subtree
    if key < root.key:
        root.left = delete(root.left, key)

    # If the kye to be delete is greater than the root's key
    # then it lies in right subtree
    elif key > root.key:
        root.right = delete(root.right, key)

    # If key is same as root's key, 
    # then this is the node to be deleted
    else:
        # Node with only one child or no child
        if not root.left:
            temp, root = root.right, None
            return temp
        elif not root.right:
            temp, root = root.left, None
            return temp

        # Node with two children:
        # Get the inorder successor (smallest in the right subtree)
        temp = min_value_node(root.right)
 
        # Copy the inorder successor's content to this node
        root.key = temp.key
 
        # Delete the inorder successor
        root.right = delete(root.right, temp.key)

    return root


if __name__ == '__main__':
 
    # Let us create the following BST
    #        50
    #     /      \
    #    30      70
    #   /  \    /  \
    #  20  40  60  80
 
    r = Node(50)

    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)
 
    # Print inoder traversal of the BST
    inorder(r)

    delete(r, 40)