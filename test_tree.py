from binary_search import make_bin_tree, get_tree_element, put_tree_element


def test_tree():
    tree = make_bin_tree()
    assert get_tree_element(tree, 0) is None
    put_tree_element(tree, 0)
    assert get_tree_element(tree, 0) == 0
    assert get_tree_element(tree, 1) is None
    put_tree_element(tree, 1)
    assert get_tree_element(tree, 1) == 1
    assert get_tree_element(tree, 0) == 0
    put_tree_element(tree, -1)
    assert get_tree_element(tree, 1) == 1
    assert get_tree_element(tree, 0) == 0
    assert get_tree_element(tree, -1) == -1
    put_tree_element(tree, -2)
    put_tree_element(tree, 2)
    assert get_tree_element(tree, 1) == 1
    assert get_tree_element(tree, 1) == 1
    assert get_tree_element(tree, 0) == 0
    assert get_tree_element(tree, -2) == -2
    assert get_tree_element(tree, 2) == 2
