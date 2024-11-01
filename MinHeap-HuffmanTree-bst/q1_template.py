import sys
import re


INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'


class MinHeap:
    class Node:
        pass

    def __init__(self):
        pass

    def bubble_up(self, index):
        pass

    def bubble_down(self, index):
        pass

    def heap_push(self, value):
        pass

    def heap_pop(self):
        pass

    def find_min_child(self, index):
        pass

    def heapify(self, *args):
        pass


class HuffmanTree:
    class Node:
        pass

    def __init__(self):
        pass

    def set_letters(self, *args):
        pass

    def set_repetitions(self, *args):
        pass

    def build_huffman_tree(self):
        pass

    def get_huffman_code_cost(self):
        pass

    def text_encoding(self, text):
        pass


class Bst:
    class Node:
        pass

    def __init__(self):
        pass

    def insert(self, key):
        pass

    def inorder(self):
        pass


class Runner:
    dsMap = {'min_heap': MinHeap, 'bst': Bst, 'huffman_tree': HuffmanTree}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, \-"\']*)\)$')

    def __init__(self, inputSrc):
        self.input = inputSrc
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            actionMethod = getattr(self, action, None)
            if actionMethod is None:
                return
            actionMethod(param)

    def make(self, params):
        itemType, itemName = params.split()
        self.items[itemName] = self.dsMap[itemType]()

    def call(self, params):
        regexRes = self.callRegex.match(params)
        itemName, funcName, argsList = regexRes.groups()

        args = [x.strip() for x in argsList.split(',')] if argsList != '' else []
        args = [x[1:-1] if x[0] in ('"', "'") else int(x) for x in args]

        method = getattr(self.items[itemName], funcName)
        try:
            result = method(*args)
        except Exception as ex:
            print(ex)
        else:
            if result is not None:
                print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
