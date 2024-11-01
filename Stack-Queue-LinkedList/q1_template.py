import sys
import re


class Queue:
    def __init__(self):
        pass

    def enqueue(self, value):
        pass

    def dequeue(self):
        pass

    def size(self):
        pass

    def empty(self):
        pass

    def one_line_str(self):
        pass


class Stack:
    def __init__(self, capacity=10):
        pass

    def push(self, value):
        pass

    def pop(self):
        pass

    def put(self, value):
        pass

    def peek(self):
        pass

    def expand(self):
        pass

    def capacity(self):
        pass

    def size(self):
        pass

    def empty(self):
        pass

    def one_line_str(self):
        pass


class Node:
    def __init__(self, value):
        pass


class LinkedList:
    def __init__(self):
        pass

    def insert_front(self, value):
        pass

    def insert_back(self, value):
        pass

    def reverse(self):
        pass

    def one_line_str(self):
        pass


class Runner:
    ds_map = {'stack': Stack, 'queue': Queue, 'linked_list': LinkedList}
    call_regex = re.compile(r'^(\w+)\.(\w+)\(([\w, ]*)\)$')

    def __init__(self, input_src):
        self.input = input_src
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            action_method = getattr(self, action, None)
            if action_method is None:
                return
            action_method(param)

    def make(self, params):
        item_type, item_name = params.split()
        self.items[item_name] = self.ds_map[item_type]()

    def call(self, params):
        regex_res = self.call_regex.match(params)
        item_name, func_name, args_list = regex_res.groups()
        args = args_list.split(',') if args_list != '' else []

        method = getattr(self.items[item_name], func_name)
        result = method(*args)
        if result is not None:
            print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
