class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedSingle:
    def __init__(self):
        self.head = None

    # Append a new Node to the end of the list
    def add(self, data):
        # Create a new Node holding the data
        newNode = Node(data)
        # If the list is empty, add the node
        if self.head is None:
            self.head = newNode
            return
        # If the list is not empty, jump to the next node until you reach the end then add the node
        oldNode = self.head
        while oldNode.next:
            oldNode = oldNode.next
        oldNode.next = newNode

    # Print the data of the list in order
    def print(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
        print("Empty")

    # Get the data at a given index
    def read(self, index):
        # Check to make sure the index is >= 0
        if index < 0:
            print("Index must be >= 0")
            return None
        # Loop through the list until the index is found
        current = self.head
        i = 0
        while current:
            if i == index:
                return current.data
            current = current.next
            i += 1
        # Handle cases where the index is larger than the length of the list
        print("Index is out of range")
        return None

    # Insert a new Node at a specified index
    def insert(self, data, index):
        # Check to make sure the index is >= 0
        if index < 0:
            print("Index must be >= 0")
            return
        # Put the data in a new Node
        newNode = Node(data)
        # Handle the case where we insert at the beginning of the list
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return
        # Loop through the list to find the specified index
        current = self.head
        for _ in range(index - 1):
            # Handle the case where the specified index is invalid
            if current is None:
                print("Index is invalid")
                return
            current = current.next
        # Now we're at the correct index, so add the Node
        newNode.next = current.next
        current.next = newNode

    # Delete the Node at a specified index
    def delete(self, index):
        # Check to make sure the index is >= 0
        if index < 0:
            print("Index must be >= 0")
            return
        # Handle the case where we're deleting the head
        if index == 0:
            if self.head:
                self.head = self.head.next
                return
            else:
                print("List is empty")
                return
        # Loop through the list to reach the node
        current = self.head
        for _ in range (index - 1):
            if current.next is None:
                print("Invalid position")
                return
            current = current.next
        # Delete the node
        if current.next:
            current.next = current.next.next


    def search(self, query):
        current = self.head
        position = 0
        while current:
            if query == current.data:
                return position
            current = current.next
            position += 1
        return None

        # do stuff

    def sort(self):
        # do stuff

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count