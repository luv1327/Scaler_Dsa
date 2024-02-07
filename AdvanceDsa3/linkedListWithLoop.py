class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_linked_list_with_loop(length, loop_index):
    if length <= 0 or loop_index < 0 or loop_index >= length:
        return None

    # Create nodes
    nodes = [ListNode(i) for i in range(1, length + 1)]

    # Connect nodes
    for i in range(length - 1):
        nodes[i].next = nodes[i + 1]

    # Create a loop by connecting the last node to the specified index
    nodes[-1].next = nodes[loop_index]

    # Return the head of the linked list
    return nodes[0]

# Example usage


# create_linked_list_with_loop(length, loop_index)

# Output the linked list

