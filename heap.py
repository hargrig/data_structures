class MaxHeap:
    def __init__(self, array: list) -> None:
        self.array = array
        self.build_heap()

    def heapify(self, N, i):
        # Initialize largest as root
        largest = i

        l = 2 * i + 1
        r = 2 * i + 2

        # If left child is larger than root
        if l < N and self.array[l] > self.array[largest]:
            largest = l

        # If right child is larger than largest so far
        if r < N and self.array[r] > self.array[largest]:
            largest = r

        # If largest is not root
        if largest != i:
            self.array[i], self.array[largest] = \
                self.array[largest], self.array[i]
            # Recursively heapify the affected sub-tree
            self.heapify(N, largest)

    def heapify_by_bottom(self, i):
        parent = int(((i-1)/2))
        # For Max-Heap
        # If current node is greater than its parent
        # Swap both of them and call heapify again for the parent
        if self.array[parent] > 0:
            if self.array[i] > self.array[parent]:
                self.array[i], self.array[parent] = self.array[parent], self.array[i]
                # Recursively heapify the parent node
                self.heapify_by_bottom(parent)

    def build_heap(self):

        N = len(self.array)

        # Index of last non-leaf node
        start_idx = N // 2 - 1

        # Perform reverse level order traversal
        # from last non-leaf node and heapify each node
        for i in range(start_idx, -1, -1):
            self.heapify(N, i)

    def print(self):
        print("Array representation of Heap is: ")
        print(self.array)
        print()

    def delete_root(self):

        N = len(self.array)

        # Get the last element
        last_element = self.array[N - 1]

        # Replace root with last element
        self.array[0] = last_element

        # Decrease size of heap by 1
        self.array.pop()
        N -= 1

        # heapify the root node
        self.heapify(N, 0)

    def insert_node(self, data: int):
        self.array.append(data)

        N = len(self.array)

        self.heapify_by_bottom(N-1)


if __name__ == '__main__':

    # array = [7,5,6,4]

    # max_heap = MaxHeap(array)
    # max_heap.heapify(4, 1)

    # max_heap.print()

    # Binary Tree Representation of input array
    #              1
    #           /     \
    #         3        5
    #       /  \      /  \
    #     4      6   13  10
    #    / \    / \
    #   9   8  15 17

    arr = [
        1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17
    ]

    print("For given array: ")
    print(arr)
    print()

    max_heap = MaxHeap(arr)
    max_heap.print()

    max_heap.delete_root()
    max_heap.print()

    max_heap.insert_node(17)

    # Final Heap: (idx) value
    # 
    #                          (0) 17
    #                      /            \
    #                     /              \
    #                    /                \
    #                   /                  \
    #               (1) 15               (2) 13 
    #                /   \                /   \
    #               /     \              /     \
    #              /       \            /       \
    #             /         \          /         \
    #          (3) 8      (4) 9     (5) 5      (6) 10
    #           /  \        /  \
    #          /    \      /    \
    #         /      \  (9) 3  (10) 6
    #      (7) 4    (8) 1 

    max_heap.print()
