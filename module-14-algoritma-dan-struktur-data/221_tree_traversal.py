class Node:
    def __init__(self, nilai, kiri=None, kanan=None):
        self.nilai, self.kiri, self.kanan = nilai, kiri, kanan


def inorder(node):
    if node is not None:
        # In-order mengunjungi kiri, node ini, lalu kanan.
        yield from inorder(node.kiri)
        yield node.nilai
        yield from inorder(node.kanan)


print("In-order:", list(inorder(Node(2, Node(1), Node(3)))))