class Node:

    def __init__(self, name, data):
        self.name = name.capitalize()
        self.data = data
        self.next = None

    def __str__(self):
        # return name of node
        return "Node name:  " + self.name + "\nData: \t\t" + str(self.data) + "\n"

class Singly_LinkedList():

    # if there is a linked list, there is at least one node
    def __init__(self, first_node_name, first_node_data):
        self.head = Node(first_node_name, first_node_data)
        print("LinkedList Create with Node: " + first_node_name +
              " \n\tNames will be automatically capitalized\n")

    def add_at_start(self, node_name, node_data):
        new_node = Node(node_name, node_data)
        new_node.next = self.head
        self.head = new_node
        print("your list looks like")

    def add_at_end(self, node_name, node_data):
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Node(node_name, node_data)

    # adds node after a specified node name

    def add_after_specified(self, specified_name, node_name, node_data):
        current_node = self.head

        while current_node.next is not None:
            if current_node.name == specified_name:
                new_node = Node(node_name, node_data)
                new_node.next = current_node.next
                current_node.next = new_node
            current_node = current_node.next

    # print the information of a spefific node
    def print_specific_info(self, specified_node_name):
        current_node = self.head

        # a generic case
        while current_node.next is not None:
            if current_node.name == specified_node_name:
                return "specified node: \n".upper() + str(current_node)
                break
            current_node = current_node.next

        # if the specified node is the last one
        if current_node.name == specified_node_name:
            return "specified node: \n".upper() + str(current_node)
        # if node is not found
        else:
            return "No such node found"

    # print how the linkedlist looks like

    def print_list(self):
        llist = ""
        current_node = self.head
        while current_node.next is not None:
            llist += current_node.name + "->"
            current_node = current_node.next
        llist += current_node.name + "->Null"
        print(llist + "\n")

    # print the information stored on every node

    def print_information(self):
        current_node = self.head
        print("full LList information".upper())
        while current_node.next is not None:
            print(current_node)
            current_node = current_node.next
        print(current_node)

    def count_nodes(self):
        num_nodes = 1
        current_node = self.head

        while current_node.next is not None:
            num_nodes += 1
            current_node = current_node.next

        return num_nodes


slinkedList = Singly_LinkedList("A", 5)
slinkedList.add_at_end("B", 6)
slinkedList.add_at_end("c", 7)
slinkedList.add_at_start("d", 4)
slinkedList.add_after_specified("A", "e", 5)

slinkedList.print_list()
slinkedList.print_information()
print(slinkedList.print_specific_info("alksdj"))

print(slinkedList.count_nodes())
