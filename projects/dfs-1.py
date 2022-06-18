# Date: 18-06-22

class Node:
    text = ''
    note = ''
    children = []

    def __init__(self, text, children=[], note=""):
        self.text = text
        self.children = children
        self.note = note

    def __str__(self) -> str:
        return f"<Node text={self.text}, note={self.note}>"

def findNodeByText(tree, text):
    visitedNodes = []
    nodesToVisit = [tree]
    while len(nodesToVisit) > 0:
        node = nodesToVisit.pop()
        if node in visitedNodes:
            continue
        if node.text == text:
            return node
        else:
            visitedNodes.append(node)
            nodesToVisit += node.children
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
    node = findNodeByText(SMALL_TREE, "2")
    print(node)
    assert node.note == "deeper"
    print("Asserts passed")

if __name__ == "__main__":
    main()