from random import choice

from tree_13.tree import SimpleTree, SimpleTreeNode


SimpleTreeNode.__repr__ = lambda x: 'Node %s' % x.NodeValue


def get_random_tree(nodes_count: int):
    t = SimpleTree(None)
    for val in range(1, nodes_count+1):
        nodes = t.GetAllNodes()
        parent = choice(nodes) if nodes else None
        t.AddChild(parent, SimpleTreeNode(val, None))
    assert t.Count() == nodes_count
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
        origNodes = tuple(orig.nodes_iterator())
        trueOrigNodes = origNodes[:origNodes.index(orig)+1]
        possible_parents = tuple(filter(lambda x: x not in trueOrigNodes, ns))
        parent = choice(possible_parents)
        t.MoveNode(orig, parent)

    assert t.LeafCount() == len([node for node in t.GetAllNodes() if not node.Children])


# --------------------------- MAIN ----------------------------------

if __name__ == '__main__':
    for n in (5, 10):
        test_get_all_and_count(n)
        test_add_find(n)
    for n, leafs in ((15, 3), (12, 4), (10000, 100)):
        test_leaf(n, leafs)

