from binary_search import make_bin_tree, get_tree_element, put_tree_element
from binary_search import delete_tree_element


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
    assert get_tree_element(tree, 0) == 0
    assert get_tree_element(tree, -2) == -2
    assert get_tree_element(tree, 2) == 2

    put_tree_element(tree, 1.5)
    put_tree_element(tree, 3)
    put_tree_element(tree, 2.5)
    put_tree_element(tree, 2.4)
    delete_tree_element(tree, 2)

    put_tree_element(tree, 2.6)
    put_tree_element(tree, 2.45)
    delete_tree_element(tree, 2.6)
    assert get_tree_element(tree, 2.6) is None

    assert get_tree_element(tree, 1) == 1
    assert get_tree_element(tree, 0) == 0
    assert get_tree_element(tree, -2) == -2
    assert get_tree_element(tree, 2) is None
    assert get_tree_element(tree, 1.5) == 1.5
    assert get_tree_element(tree, 3) == 3
    assert get_tree_element(tree, 2.5) == 2.5
    assert get_tree_element(tree, 2.4) == 2.4

    delete_tree_element(tree, 3)
    assert get_tree_element(tree, 3) is None
    assert get_tree_element(tree, 2.5) == 2.5
    assert get_tree_element(tree, 2.45) == 2.45

    put_tree_element(tree, 2.7)
    put_tree_element(tree, 2.8)
    delete_tree_element(tree, 2.7)
    assert get_tree_element(tree, 2.7) is None
    assert get_tree_element(tree, 2.8) == 2.8
