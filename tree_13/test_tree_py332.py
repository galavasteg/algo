from random import choice

from tree_13.tree import SimpleTree, SimpleTreeNode


SimpleTreeNode.__repr__ = lambda x: 'Node %s' % x.NodeValue


def splitOnChunks(iterable, chunk_size: int) -> dict:
    """Yield successive splitOnChunks from *iterable*."""
    for i in range(0, len(iterable), chunk_size):
        chunk = iterable[i:i + chunk_size]
        n = len(chunk)
        start, end = i + 1, i + n
        yield {'0': start, '1': end, 'count': n, 'chunk': chunk}


def get_random_tree(nodes_count: int):
    t = SimpleTree(None)
    for val in range(1, nodes_count+1):
        nodes = t.GetAllNodes()
        parent = choice(nodes) if nodes else None
        t.AddChild(parent, SimpleTreeNode(val, None))
    assert t.Count() == nodes_count
    return t


def get_one_branch_tree(nodes: int, reverse=False):
    t = SimpleTree(None)
    prev_node = None
    r = range(nodes-1, -1, -1) if reverse else range(nodes)
    for i in r:
        new_node = SimpleTreeNode(i, prev_node)
        t.AddChild(prev_node, new_node)
        prev_node = new_node
    assert t.LeafCount() == 1
    assert t.Count() == nodes
    return t


# --------------------------- TESTS ---------------------------------

def test_get_all_and_count(n: int):
    t = get_random_tree(n)
    ns = t.GetAllNodes()
    assert set(map(lambda x: x.NodeValue, ns)) == set(range(1, n+1))
    assert t.Count() == n


def test_add_find(n: int):
    t = get_random_tree(n)
    assert t.FindNodesByValue(1) == [t.Root]

    t.AddChild(t.Root, SimpleTreeNode('new', None))
    assert any(node.NodeValue == 'new' for node in t.Root.Children)

    val = '=)'
    for vals_count in range(1, 1000):
        t.AddChild(choice(t.GetAllNodes()), SimpleTreeNode(val, None))
        found_nodes = t.FindNodesByValue(val)
        assert len(found_nodes) == vals_count


def test_del(n: int):
    t = get_one_branch_tree(n, reverse=True)
    for val in range(n-1):
        t.DeleteNode(t.FindNodesByValue(val)[0])
        assert not t.FindNodesByValue(val)
    assert t.Count() == 1


def test_move(n: int):
    t = get_one_branch_tree(n)

    half = n // 2
    [orig] = t.FindNodesByValue(half)
    prev_parent = orig.Parent
    init_count = t.Count()
    origNodes = tuple(orig.post_order_nodes_iterator())

    t.MoveNode(orig, t.Root)
    assert orig not in prev_parent.Children
    assert orig in t.Root.Children
    assert len(t.Root.Children) == 2
    assert orig.level == 1 and orig.NodeValue == half
    assert all(node.level == 2 for node in orig.Children)
    assert init_count == t.Count()
    assert origNodes == tuple(orig.post_order_nodes_iterator())


def test_random_move(count):
    t = get_one_branch_tree(count)

    ns = t.GetAllNodes()
    non_root_ns = tuple(n for n in ns if n is not t.Root)
    for _ in range(100):
        orig = choice(non_root_ns)
        origNodes = tuple(orig.post_order_nodes_iterator())
        trueOrigNodes = origNodes[:origNodes.index(orig)+1]
        possible_parents = tuple(filter(lambda x: x not in trueOrigNodes, ns))
        parent = choice(possible_parents)

        prev_parent = orig.Parent
        p_lvl, children_n = parent.level, len(parent.Children)

        t.MoveNode(orig, parent)
        assert orig in parent.Children
        if parent is not prev_parent:
            assert orig not in prev_parent.Children
            assert len(parent.Children) == children_n + 1
        assert orig.level == p_lvl + 1
        assert all(n.level == orig.level + 1
                   for n in orig.Children)
        assert t.Count() == count
        assert len(origNodes) != tuple
        origNodes_ = tuple(orig.post_order_nodes_iterator())
        trueOrigNodes_ = origNodes_[:origNodes_.index(orig)+1]
        assert trueOrigNodes == trueOrigNodes_

    assert t.Count() == count
    assert len(set(t.GetAllNodes())) == count
    return t


def test_leaf(n: int, leafs: int):
    t = SimpleTree(SimpleTreeNode('root', None))
    for c in splitOnChunks(range(n), n // leafs):
        parent = t.Root
        # parent: SimpleTreeNode
        for val in c['chunk']:
            node = SimpleTreeNode(val, None)
            t.AddChild(parent, node)
            parent = node

    assert t.LeafCount() == leafs
    assert t.Count() == n + 1

    ns = t.GetAllNodes()
    non_root_ns = tuple(n for n in ns if n is not t.Root)
    for _ in range(10):
        orig = choice(non_root_ns)
        origNodes = tuple(orig.post_order_nodes_iterator())
        trueOrigNodes = origNodes[:origNodes.index(orig)+1]
        possible_parents = tuple(filter(lambda x: x not in trueOrigNodes, ns))
        parent = choice(possible_parents)
        t.MoveNode(orig, parent)

    assert t.LeafCount() == len(
        [node for node in t.GetAllNodes() if not node.Children])
    assert t.Count() == n + 1


def test_even_trees():
    t = SimpleTree(None)
    et = t.EvenTrees()
    assert et == []

    t = get_one_branch_tree(1)
    et = t.EvenTrees()
    assert et == []

    t = get_one_branch_tree(2)
    et = t.EvenTrees()
    assert et == []

    t = get_one_branch_tree(4)
    et = t.EvenTrees()
    assert et == [t.Root.Children[0], t.Root.Children[0].Children[0]]

    root = SimpleTreeNode(1, None)
    t = SimpleTree(root)
    n2 = SimpleTreeNode(2, root)
    n3 = SimpleTreeNode(3, root)
    n6 = SimpleTreeNode(6, root)
    [t.AddChild(root, c) for c in (n2, n3, n6,)]
    n5 = SimpleTreeNode(5, n2)
    n7 = SimpleTreeNode(7, n2)
    [t.AddChild(n2, c) for c in (n5, n7,)]
    n4 = SimpleTreeNode(4, n3)
    t.AddChild(n3, n4)
    n8 = SimpleTreeNode(8, n6)
    t.AddChild(n6, n8)
    n9 = SimpleTreeNode(9, n6)
    n10 = SimpleTreeNode(10, n6)
    [t.AddChild(n8, c) for c in (n9, n10,)]
    et = t.EvenTrees()
    assert et == [
            root, n3,
            root, n6,
        ]

    n11 = SimpleTreeNode(11, n5)
    n12 = SimpleTreeNode(12, n7)
    t.AddChild(n5, n11)
    t.AddChild(n7, n12)
    et = t.EvenTrees()
    assert et == [
            n2, n5,
            n2, n7,
            root, n3,
            root, n6,
        ]

    n13 = SimpleTreeNode(11, n8)
    n14 = SimpleTreeNode(12, n8)
    [t.AddChild(n8, c) for c in (n13, n14,)]
    et = t.EvenTrees()
    assert et == [
            n2, n5,
            n2, n7,
            root, n3,
            root, n6,
        ]

    n15 = SimpleTreeNode(15, n11)
    n16 = SimpleTreeNode(16, n12)
    t.AddChild(n11, n15)
    t.AddChild(n12, n16)
    et = t.EvenTrees()
    assert et == [
            n5, n11,
            n7, n12,
            root, n3,
            root, n6,
        ]


# --------------------------- MAIN ----------------------------------

if __name__ == '__main__':
    for n in (5, 10):
        test_get_all_and_count(n)
        test_add_find(n)
    for n in (6, 10, 100):
        test_move(n)
        test_del(n)
    t = test_random_move(1000)

    test_even_trees()

    for n, leafs in ((15, 3), (12, 4), (10000, 100)):
        test_leaf(n, leafs)

