# https://www.hackerrank.com/challenges/xml-1-find-the-score/problem
import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    c = len(node.attrib)
    for child in node:
        c += get_attr_number(child)

    return c


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
