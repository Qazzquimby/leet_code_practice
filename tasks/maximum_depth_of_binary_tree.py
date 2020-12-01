import typing as t
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return (isinstance(other, TreeNode)
                and self.val == other.val
                and self.left == other.left
                and self.right == other.right)

    def __str__(self):
        left = "" if self.left is None else str(self.left)
        right = "" if self.right is None else str(self.right)

        return f"{self.val}({left}, {right})"


def get_current_depth(index):
    return math.ceil(math.log(index + 2) / math.log(2))


def get_left(index: int, flattened: t.List[int]):
    left_index = 2 * index + 1
    try:
        return get_node(left_index, flattened)
    except IndexError:
        return None


def get_right(index: int, flattened: t.List[int]):
    right_index = 2 * index + 2
    try:
        return get_node(right_index, flattened)
    except IndexError:
        return None


def get_node(index: int, flattened: t.List[int]):
    return TreeNode(flattened[index], get_left(index, flattened), get_right(index, flattened))


def make_tree(flattened: t.List[int]):
    return get_node(index=0, flattened=flattened)


def get_flattened_tree_depth(flattened: t.List[int]):
    depth = math.ceil(math.log(len(flattened) + 1) / math.log(2))
    return depth


def get_tree_depth(node: TreeNode) -> int:
    if node is None:
        return 0
    return 1 + max(get_tree_depth(node.left), get_tree_depth(node.right))
