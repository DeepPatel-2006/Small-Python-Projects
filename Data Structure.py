class Node: # Node Class
    
    def __init__(self, value, next_node = None): # instance function

        self.value = value
        self.next_node = next_node

    def get_value(self): # gets the nodes value

        return self.value
    
    def get_next_node(self): # gets the next node

        return self.next_node
    
    def set_next_node(self, next_node): # sets the next node of the original node
        self.next_node = next_node


class LinkedList: # linkedlist class
    
    def __init__(self, value = None): # instance function

        self.head_node = Node(value)

    def get_head_node(self): # gets the head node
        
        return self.head_node
    
    def insert_beginning(self, new_value): # inserts the head node a linked list

        new_node = Node(new_value)
        new_node.set_next_node(self.get_head_node)
        self.head_node = new_node

    def stringify_list(self): # returns a string where each line is the value of a node in the linked list
        string_list = ''

        current_node = self.get_head_node()

        while current_node:

            if current_node.get_value() != None:

                string_list += str(current_node.get_value()) + '\n'


            current_node = current_node.get_next_node()
        
        return string_list

    def remove_node(self, value_to_remove): # removes a node of a list with a given value
        current_node = self.get_head_node()
        
        if current_node.get_value() == value_to_remove:
            
            self.head_node = self.get_head_node.get_next_node()
        else:
            while current_node:

                next_node = current_node.get_next_node()

                if next_node.get_value() == value_to_remove:
                    
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

class BinaryTreeNode: # binary tree class
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None