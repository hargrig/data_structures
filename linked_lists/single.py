class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data: int):
        # 1. Allocate the Node &
        # 2. Put in the data
        new_node = Node(new_data)
        # 3. Make next of new Node as head
        new_node.next = self.head
        # 4. Move the head to point to new Node
        self.head = new_node

        return self

    def insert_after(self, prev_node: Node, new_data: int):
        # 1. check if the given prev_node exists
        if not prev_node: return self

        # 2. Create new node
        # 3. Put in the data
        new_node = Node(new_data)
        # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next
        # 5. make next of prev_node as new_node
        prev_node.next = new_node

        return self

    def append(self, new_data: int):
        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)

        # 4. If the Linked List is empty, then make the new node as head
        if not self.head:
            self.head = new_node
            return self

        # 5. Else traverse till the last node
        last = self.head
        while last.next: last = last.next

        # 6. Change the next of last node
        last.next = new_node

        return self

    def traverse(self):
        """ Traverse linked list printing values in it

        """
        temp = self.head

        while temp: 
            print(temp.data),
            temp = temp.next


if __name__=='__main__':
    linked_list = LinkedList()
    
    # 1 -> 7-> 8-> 6-> 4-> None
    linked_list.append(6)\
        .push(7)\
        .push(1)\
        .append(4)\
        .insert_after(linked_list.head.next, 10)
 
    print('Created linked list is: ')
    linked_list.traverse()