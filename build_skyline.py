# create a node class to represent avl binary search tree
# we first define the possible children locations the node can have, which for a binary tree is left and right
# we define the value of the node itself
# we define the instrinsic property, height, of our current node (it will be updated for insertion and deletion)
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.height = 1

# need to find a way to retrieve height and define the difference in height
# if the node does not exist, there is no height, otherwise, just return the height
def height(node):
    if not node:
        return 0

    return node.height

# helper function to update a node's height, which is calculated by the largest subtree's height + 1
def heightUpdate(node):
    return (1 + max(height(node.left), height(node.right)))

# balance/skew is defined as the difference between the left child's height and the right child's height
def balance(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

# for avl trees, we need rotations. so left and right rotate
# for a left rotate operation, to maintain in place BST, right child of node is rooted and node will be new root's left child. then right child's left child will be node's right child. heights will be updated, and the new rooted node will be returned
def leftRotate(node):
    if node.left != None or node.right != None:
        rChild = node.right
        rlChild = rChild.left
        rChild.left = node
        node.right = rlChild

        node.height = heightUpdate(node)
        rChild.height = heightUpdate(rChild)
        return rChild

# right rotate will function similarly, but flipped.
def rightRotate(node):
    if node.left != None or node.right !=None:
        lChild = node.left
        lrChild = lChild.right
        lChild.right = node
        node.left = lrChild

        node.height = heightUpdate(node)
        lChild.height = heightUpdate(lChild)
        return lChild

# findMin and findMax
# min is defined as the "left-most node" since an in-place sort will touch the leftmost node first.
def findMin(node):
    while node.left:
        node = node.left

    return node

# max is the right-most since in-place will reach right last
def findMax(node):
    while node.right:
        node = node.right

    return node

# insert and delete
# insertion will insert when it reaches the correct position to insert
# this is done by comparing the keys to the current node and will recurse left or right accordingly until it fits the in-place rule
# afterwards, the height is updated
def insert(node, key):

    if not node:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    node.height = heightUpdate(node)

    # balance is checked after each addition to make sure the avl tree is balanced
    # cases similar in class:
    # if left is larger than 1, we check values and if current key is smaller than left child's key, right rotate; otherwise, left rotate the left child and then right rotate the entire node
    # the reverse case holds for right child's height being larger than 1
    currentBalance = balance(node)

    if currentBalance > 1:
        if key < node.left.key:
            return rightRotate(node)
        else:
            node.left = leftRotate(node.left)
            return rightRotate(node)
    if currentBalance < -1:
        if key >= node.right.key:
            return leftRotate(node)
        else:
            node.right = rightRotate(node.right)
            return leftRotate(node)

    return node

# deleting will replace the node until it becomes a leaf, maintaining in-place
def delete(node, key):

    if not node:
        return node

    if key < node.key:
        node.left = delete(node.left, key)
    elif(key > node.key):
        node.right = delete(node.right, key)
    else:
        if not node.left:
            temp = node.right
            node = None
            return temp
        elif not node.right:
            temp = node.left
            node = None
            return temp

        temp = findMin(node.right)
        node.key = temp.key
        node.right = delete(node.right, temp.key)

    node.height = heightUpdate(node)

    # same balance as insert
    currentBalance = balance(node)

    if currentBalance > 1:
        if balance(node.left) >= 0:
            return rightRotate(node)
        else:
            node.left = leftRotate(node.left)
            return rightRotate(node)

    if currentBalance < -1:
        if balance(node.right) <= 0:
            return leftRotate(node)
        else:
            node.right = rightRotate(node.right)
            return leftRotate(node)

    return node

"""
main function, build_skyline(), where input is in the form of a list of buildings, B, and outputs the skyline, S, as a list
"""
def build_skyline(B):

    # initialize root, locations, skyline (final output), and corners
    root = None
    locations = dict()
    skyline = []
    corners = []

    # labels each corner accordingly
    for building in B:
        (left, height, right) = building
        corners.append((left, height, "left"))
        corners.append((right, height, "right"))

    corners.sort() # n log n sort
    currentHeight = 0 # initial height

    # goes through each corner and checks if left or right direction
    # inserts for left; deletes for right
    # then, it adds the height for left and the remaining max height for right
    for corner in corners:
        (location, height, direction) = corner

        if direction == "left":
            root = insert(root, height)

            if currentHeight < height:
                locations[location] = height
                currentHeight = height
        if direction == "right":
            root = delete(root, height)
            if root:
                maxHeight = findMax(root).key
            else:
                maxHeight = 0
            if currentHeight > maxHeight:
                locations[location] = maxHeight
                currentHeight = maxHeight

    # since locations has been undated to remove "useless" corners, skyline will be a list form of this dictionary
    for key in locations:
        skyline.append((key, locations[key]))

    return skyline
