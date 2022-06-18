# Date: 18.06.22
# Algorithm: BFS
# TODO: big O

class Node:
    text = ''
    children = []
    note = ''

    def __init__(self, text, children=[], note=''):
        self.text = text
        self.children = children
        self.note = note

    def __repr__(self):
        return f'<Node text={self.text} children={repr(self.children)} note={self.note}>'

def findNodeByText(tree, text):
    visitedNodes = []
    nodesToVisit = [tree]
    while len(nodesToVisit) > 0:
        node = nodesToVisit.pop()
        print(f'Visiting node: {repr(node)}')
        if node.text == text:
            print("Node matched. Returning.")
            return node
        print('Node did not match.')
        if node in visitedNodes:
            continue
        else:
            visitedNodes.append(node)
        for child in node.children:
            visitedNodes
            nodesToVisit.append(child)
            print(f'Adding node to queue: {repr(child)}')
        nodesToVisit.reverse()
    return None


SMALL_TREE = Node("1",[
        Node("2", [], "breadther"),
        Node("3"),
        Node("4", [
            Node("5"),
            Node("2", [], "deeper")
        ])
    ])

def main():
    foundNode = findNodeByText(SMALL_TREE, "2")
    print(f'Found node: {repr(foundNode)}')
    assert foundNode.note == "breadther"
    print("All asserts passed")

if __name__ == '__main__':
    main()