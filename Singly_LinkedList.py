class Node:

    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.next = None

    def __str__(self):
        # return name of node
        return "This is node: " + self.name

class LinkedList():

    def __init__(self):
        self.head = None
        print("LinkedList Created. Names will be automatically capitalized")

    def add_at_start(self, node_name, node_data):
        new_node = Node(node_name, node_data)
        new_node.next = self.head
        self.head = new_node

    def add_at_end(self, node_name, node_data):
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Node(node_name, node_data)

    def add_after_specified(self, specified_name, node_name, node_data):
        current_node = self.head

        while current_node.next is not None:
            if current_node.name == specified_name:
                new_node = Node(node_name, node_data)
                new_node.next = current_node.next
                current_node.next = new_node
            current_node = current_node.next

    def print_list(self):
        llist = ""
        current_node = self.head
        while current_node.next is not None:
            llist += current_node.name + "->"
            current_node = current_node.next
        llist += current_node.name + "->x"
        print(llist)

    def print_schedule_information(self):
        current_node = self.head
        while current_node.next is not None:
            print(current_node)
            current_node = current_node.next
        print(current_node)


schedule = LinkedList()
schedule.head = Node("a", 5)
schedule.add_at_end("B", 6)
schedule.add_at_end("c", 7)
schedule.add_at_start("d", 4)
schedule.add_after_specified("A", "e", 5)

schedule.print_list()
