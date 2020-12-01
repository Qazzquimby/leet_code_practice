from tasks.maximum_depth_of_binary_tree import make_tree, get_flattened_tree_depth, TreeNode, get_tree_depth


def test_make_tree__when_1_item__1_node():
    actual = make_tree([3])
    expected = TreeNode(3)
    assert expected == actual


def test_make_tree__when_3_item__1_with_children():
    actual = make_tree([3, 4, 5])
    expected = TreeNode(3,
                        left=TreeNode(4),
                        right=TreeNode(5)
                        )
    assert expected == actual


def test_make_tree__when_7_item__3_with_children():
    actual = make_tree([3, 4, 5, 6, 7, 8, 9])
    expected = TreeNode(3,
                        left=TreeNode(4,
                                      left=TreeNode(6),
                                      right=TreeNode(7)),
                        right=TreeNode(5,
                                       left=TreeNode(8),
                                       right=TreeNode(9))
                        )
    assert expected == actual


def test_get_tree_depth__when_1_item__1():
    actual = get_tree_depth(TreeNode(3))
    expected = 1
    assert expected == actual


def test_get_tree_depth__when_2_item__2():
    actual = get_tree_depth(TreeNode(3,
                                     left=TreeNode(4)))
    expected = 2
    assert expected == actual
