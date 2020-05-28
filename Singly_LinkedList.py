class Node:

    def __init__(self, name, data):
        self.name = name.capitalize()
        self.data = data
        self.next = None

    def __str__(self):
        # return name of node
        return "Node name:  " + self.name + "\nData: \t\t" + str(self.data) + "\n"

class LinkedList():

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

    def add_after_specified(self, specified_name, node_name, node_data):
        current_node = self.head

        while current_node.next is not None:
            if current_node.name == specified_name:
                new_node = Node(node_name, node_data)
                new_node.next = current_node.next
                current_node.next = new_node
            current_node = current_node.next

    def print_specific_info(self, specified_node_name):
        current_node = self.head

        while current_node.next is not None:
            if current_node.name == specified_node_name:
                print("specified node: \n".upper() +
                      str(current_node))
                break
            current_node = current_node.next


def print_list(linked_list):
    llist = ""
    current_node = linked_list.head
    while current_node.next is not None:
        llist += current_node.name + "->"
        current_node = current_node.next
    llist += current_node.name + "->Null"
    print(llist + "\n")


def print_information(linked_list):
    current_node = linked_list.head
    print("full LList information".upper())
    while current_node.next is not None:
        print(current_node)
        current_node = current_node.next
    print(current_node)


schedule = LinkedList("A", 5)
schedule.add_at_end("B", 6)
schedule.add_at_end("c", 7)
schedule.add_at_start("d", 4)
schedule.add_after_specified("A", "e", 5)

print_list(schedule)
print_information(schedule)
