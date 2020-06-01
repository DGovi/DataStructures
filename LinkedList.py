class Node:

    def __init__(self, name, data):
        self.name = name.capitalize()
        self.data = data
        self.next = None
        self.previous = None
        print("Node Added")

    def __str__(self):
        # return name of node
        return "Node name:  " + self.name + "\nData: \t\t" + str(self.data) + "\n"

class Singly_LinkedList():

    # if there is a linked list, there is at least one node
    def __init__(self, first_node_name, first_node_data):
        print("Singly Linked List created")
        self.head = Node(first_node_name, first_node_data)

        # print how the linkedlist looks like

    def __str__(self):
        llist = ""
        current_node = self.head
        while current_node.next is not None:
            llist += current_node.name + "->"
            current_node = current_node.next
        llist += current_node.name + "->Null"
        return "your list looks like\n" + llist + "\n"

    def add_at_start(self, node_name, node_data):
        new_node = Node(node_name, node_data)
        new_node.next = self.head
        self.head = new_node

    def delete_first_node(self):
        delete_node = self.head
        self.head = self.head.next
        del delete_node
        print("deleted a node")

    def add_at_end(self, node_name, node_data):
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Node(node_name, node_data)

    def delete_last_node(self):
        current_node = self.head

        while current_node.next.next is not None:
            current_node = current_node.next

        del current_node.next
        current_node.next = None
        print("deleted a node")

    # adds node after a specified node name

    def add_after_specified(self, specified_name, node_name, node_data):
        current_node = self.head

        while current_node.next is not None:
            if current_node.name == specified_name:
                new_node = Node(node_name, node_data)
                new_node.next = current_node.next
                current_node.next = new_node
            current_node = current_node.next

    def delete_specified_node(self, specified_node_name):
        current_node = self.head

        while current_node.next is not None:
            if current_node.next.name == specified_node_name:
                current_node.next = current_node.next.next
                break
            current_node = current_node.next
        print("deleted a node")

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
            return "No such node with name: \n\t" + specified_node_name + "\n"

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


'''
# linkedlist creation methods
slinkedList = Singly_LinkedList("A", 5)
slinkedList.add_at_end("B", 6)
slinkedList.add_at_end("c", 7)
slinkedList.add_at_start("sausage", 6)
slinkedList.add_at_start("d", 4)
slinkedList.add_after_specified("A", "E", 5)
print(slinkedList)
print(slinkedList.count_nodes())
print("=" * 100)


# linked list delteion functions
slinkedList.delete_first_node()
slinkedList.delete_last_node()
slinkedList.delete_specified_node("A")
print(slinkedList)
# slinkedList.print_information()
print(slinkedList.print_specific_info("alksdj"))
print(slinkedList.print_specific_info("A"))

print(slinkedList.count_nodes())
'''

class Doubly_LinkedList(Singly_LinkedList):

    def __init__(self, node_name, node_data):
        print("Doubly Linked list created")
        self.head = Node(node_name, node_data)

    def __str__(self):
        llist = "Null<-"
        current_node = self.head
        while current_node.next is not None:
            llist += current_node.name + "<-->"
            current_node = current_node.next
        llist += current_node.name + "->Null"
        return "your list looks like\n" + llist + "\n"

    def add_at_end(self, node_name, node_data):
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Node(node_name, node_data)
        current_node.next.previous = current_node

    def delete_first_node(self):
        delete_node = self.head
        self.head = self.head.next
        self.head.previous = None
        del delete_node
        print("deleted a node")

    # adds node after a specified node name
    def add_after_specified(self, specified_name, node_name, node_data):
        current_node = self.head

        while current_node.next is not None:
            if current_node.name == specified_name:
                new_node = Node(node_name, node_data)
                current_node.next.previous = new_node
                new_node.next = current_node.next
                current_node.next = new_node
                new_node.previous = current_node
            current_node = current_node.next

    def delete_specified_node(self, specified_node_name):
        current_node = self.head

        while current_node.next is not None:
            if current_node.next.name == specified_node_name:
                current_node.next = current_node.next.next
                current_node.next.previous = current_node
                break
            current_node = current_node.next
        print("deleted a node")


dlinkedList = Doubly_LinkedList("A", 5)
dlinkedList.add_at_end("B", 6)
dlinkedList.add_at_end("c", 7)

dlinkedList.add_at_start("sausage", 6)
dlinkedList.add_at_start("d", 4)
dlinkedList.add_after_specified("A", "E", 5)

print(dlinkedList.count_nodes())
print(dlinkedList)
print("=" * 100)

# linked list delteion functions
dlinkedList.delete_first_node()
dlinkedList.delete_last_node()
dlinkedList.delete_specified_node("A")
print(dlinkedList)

dlinkedList.print_information()
print(dlinkedList.print_specific_info("alksdj"))
print(dlinkedList.print_specific_info("E"))

print(dlinkedList.count_nodes())
