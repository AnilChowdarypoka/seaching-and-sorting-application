import random


class CreateNode:
    def __init__(self, node_value):
        self.node_value = node_value
        self.left_value = None
        self.right_value = None


class BST:
    def __init__(self):
        self.root = None

    def insert_data(self, data):
        if not self.root:
            self.root = CreateNode(data)
            return
        node_obj = self.root
        while True:
            if data < node_obj.node_value:
                if not node_obj.left_value:
                    node_obj.left_value = CreateNode(data)
                    break
                node_obj = node_obj.left_value
            else:
                if not node_obj.right_value:
                    node_obj.right_value = CreateNode(data)
                    break
                node_obj = node_obj.right_value

    def search_element(self, val):
        return self.get_searched_element(self.root, val)

    def get_searched_element(self, node=None, val=None):

        if not node:
            return False
        if node.node_value == val:
            return True
        elif val < node.node_value:
            return self.get_searched_element(node.left_value, val)
        else:
            return self.get_searched_element(node.right_value, val)


class BinarySearchTree:

    def __init__(self, data):
        self.data = data
        self.bst = self.create_bst(data)

    def create_bst(self, input_value):
        bst = BST()
        for i in self.data:
            bst.insert_data(i)
        return bst

    def search_element(self, val):
        return self.bst.search_element(val)
