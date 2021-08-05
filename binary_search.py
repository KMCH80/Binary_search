# Создать структуру бинарного дерева поиска
# Если в структуре нет элементов, то создается нулевой узел
# Если элемент присутствует, то сравниваем с ним
# Если новый элемент меньше, то добавляем в ребенка слева
# Если новый элемент больше, то добавляем в ребенка справа
import copy


def make_bin_tree():
    dic = {}
    return dic


def get_tree_element(tree, element):
    if 'root' not in tree:
        return None
    if tree.get('root') == element:
        return element
    if element >= tree['root']:
        if tree.get('right_child') is not None and get_tree_element(
                tree['right_child'], element) == element:
            return element
        else:
            return None
    else:
        if tree.get('left_child') is not None and get_tree_element(
                tree['left_child'], element) == element:
            return element
        else:
            return None


# {root: 0, left_child: {root: -1, left_child: {root: -2}, right_child: None}, right_child: {root: 1, left_child: NONE, right_child: NONE}}
def put_tree_element(tree, element):
    if tree.get('root') is not None:
        if element >= tree['root']:
            if 'right_child' not in tree:
                tree['right_child'] = make_bin_tree()
            put_tree_element(tree['right_child'], element)
        else:
            if 'left_child' not in tree:
                tree['left_child'] = make_bin_tree()
            put_tree_element(tree['left_child'], element)
    else:
        tree['root'] = element


# Операция удаления..
def delete_tree_element(tree, element):
    if tree.get('root') is not None:
        if tree['root'] == element:
            if tree.get('right_child') is None and tree.get(
                    'left_child') is None:
                tree.pop('root')
                return
            if tree.get('right_child') is None and tree.get(
                    'left_child') is not None:
                new_tree = copy.deepcopy(tree['left_child'])
                tree['root'] = new_tree['root']
                if new_tree.get('left_child') is not None:
                    tree['left_child'] = new_tree['left_child']
                if new_tree.get('right_child') is not None:
                    tree['right_child'] = new_tree['right_child']
                return
            if tree.get('right_child') is not None and tree.get(
                    'left_child') is None:
                new_tree = copy.deepcopy(tree['right_child'])
                tree['root'] = new_tree['root']
                if new_tree.get('left_child') is not None:
                    tree['left_child'] = new_tree['left_child']
                if new_tree.get('right_child') is not None:
                    tree['right_child'] = new_tree['right_child']
                return
            if tree.get('right_child') is not None and tree.get(
                    'left_child') is not None:
                tree['root'] = pop_min_element(tree['right_child'])
                return
        else:
            if element >= tree['root'] and 'right_child' in tree:
                delete_tree_element(tree['right_child'], element)
                return
            if element < tree['root'] and 'left_child' in tree:
                delete_tree_element(tree['left_child'], element)


def pop_min_element(tree):
    if 'left_child' not in tree:
        element = tree['root']
        tree.pop('root')
        return element
    return pop_min_element(tree['left_child'])
