import xml.etree.ElementTree as etree

maxdepth = 0


def depth(node, level):
    global maxdepth
    if level == -1:
        level += 1
    maxdepth = max(maxdepth, level)
    for child in node:
        depth(child, level + 1)


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
