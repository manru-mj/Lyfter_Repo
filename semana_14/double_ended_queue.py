class Node:
    def __init__(self, data:str, next:"Node"=None):
        self.data = data
        self.next = next

class Double_Ended_Queue:
    def __init__(self, head:Node=None):
        self.head = head
        self.tail = head
        self.penultimate = None


    def push_right(self,new_data):
        current_node = Node(new_data)
        
        if self.head is None: #if empty
            self.head = self.tail = current_node
            self.penultimate = None
        elif self.head.next is None: # there is only one node
            self.penultimate = self.head
            self.head.next = current_node
            self.tail = current_node
        else:# more than one node
            self.penultimate = self.tail
            self.tail.next = current_node
            self.tail = current_node


    def push_left(self,new_data):
        current_node = Node(new_data)
        
        if self.head is None: #if empty
            self.head = self.tail = current_node
            self.penultimate = None
        else: # there is only one node
            current_node.next = self.head
            self.head = current_node
            
            if self.head.next == self.tail: #if there was only one node
                self.penultimate = self.head.next


    def pop_left(self):
        if self.head is not None:
            self.head = self.head.next
        else:
            print("Queue is empty")


    def pop_right(self):
        if self.head is None:#if empty
            print("Queue is empty")
            return
        if self.head == self.tail: # there is only one node
            self.head = self.tail = self.penultimate = None
        elif self.penultimate is not None:# more than one node
            self.tail = self.penultimate
            self.tail.next = None

            if self.head == self.tail:
                self.penultimate = None
            else:
                current_node = self.head
                while current_node.next != self.tail:
                    current_node = current_node.next
                self.penultimate = current_node


    def print_structure(self):
        current_node = self.head
        if current_node is not None:
            while current_node is not None:
                print(current_node.data)
                current_node = current_node.next
        else:
            print("Queue is empty")


new_node = Node("zero")
new_double_ended_queue = Double_Ended_Queue(new_node)


new_double_ended_queue.push_left("one")
new_double_ended_queue.push_right("two")
new_double_ended_queue.push_left("three")
new_double_ended_queue.push_right("four")
print("Nodes added to have odd number before zero and even numbers after zero.")
new_double_ended_queue.print_structure()

new_double_ended_queue.pop_left()
new_double_ended_queue.pop_left()
new_double_ended_queue.pop_right()
print("New queue after removing 2 nodes from the left and 1 from the right.")
new_double_ended_queue.print_structure()