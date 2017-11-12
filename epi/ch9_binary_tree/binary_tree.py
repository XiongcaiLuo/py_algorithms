# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def preorder(root):
    if root is None:
        return
    stack = []
    stack.append(root)
    while stack:
        cur = stack.pop()
        print cur.key
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)


def inorder(root):
    if root is None:
        return
    stack = []
    _push_all_left(root, stack)
    while stack:
        cur = stack.pop()
        print cur.key
        _push_all_left(cur.right, stack)


def _push_all_left(root, stack):
    if root is None:
        return
    while root:
        stack.append(root)
        root = root.left


def postorder(root):
    if root is None:
        return
    stack = []
    stack.append([root, 0]) # 1 表示peeked， 0 表示还没有peeked
    while stack:
        pair = stack[-1]
        if pair[1] == 1:
            stack.pop()
            print pair[0].key
        else:
            if pair[0].right:
                stack.append([pair[0].right,0])
            if pair[0].left:
                stack.append([pair[0].left, 0])
            pair[1] = 1 # peeked


def persist(root, order='level'):
    stack = []
    if order == 'level':
        _persist_by_level(root, stack)
    elif order == 'preorder':
        _persist_by_preorder(root, stack)
    elif order == 'postorder':
        _persist_by_postorder(root, stack)
    return stack

def _persist_by_level(root, stack):
    pass

def _persist_by_preorder(root, stack): # 使用非递归方式也非常方便
    if root is None:
        stack.append('#')
        return stack
    stack.append(root.key)
    _persist_by_preorder(root.left, stack)
    _persist_by_preorder(root.right, stack)


def _persist_by_postorder(root, stack):
    pass

def recover(symbols, order='level'):
    if order == 'level':
        return _recover_by_level(symbols)
    elif order == 'preorder':
        return _recover_by_preorder(symbols)
    elif order == 'postorder':
        return _recover_by_postorder(symbols)

def _recover_by_level(symbols):
    if not symbols:
        return None
    pass


def _recover_by_preorder(symbols):
    if not symbols:
        return None



def _recover_by_postorder(symbols):
    if not symbols:
        return None
    pass


def _example_tree():
    keys = ['H', 'B', 'C', 'F', 'E', 'D', 'A', 'G', 'I']
    nodes = [Node(x) for x in keys]
    maps = {}
    for i in range(len(keys)):
        maps[keys[i]] = nodes[i]
    root = maps['H']
    maps['H'].left, maps['H'].right = maps['B'], maps['C']
    maps['B'].left, maps['B'].right = maps['F'], maps['E']
    maps['E'].left = maps['A']
    maps['C'].right = maps['D']
    maps['D'].right = maps['G']
    maps['G'].left = maps['I']
    return root


class Trie(object):
    class Node(object):
        def __init__(self):
            pass
            
        def __del__(self):
            pass
            
        def __exit__(self):
            pass
    
    def __init__(self):
        pass

    def insert(self, strs):
        pass

    def search(self, target):
        pass

    def common_prefix(self, target):
        pass

if __name__ == '__main__':
    root = _example_tree()
    # preorder(root)
    # inorder(root)
    # postorder(root)
    print persist(root, order='preorder')