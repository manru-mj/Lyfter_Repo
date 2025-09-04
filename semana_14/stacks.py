class Node:
    def __init__(self, data:str, next:"Node"=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self, head:Node=None):
        self.head = head

    def push(self,new_data):
        current_node = Node(new_data,self.head)
        self.head = current_node


    def pop(self):
        if self.head is not None:
            self.head = self.head.next
        else:
            print("Stack is empty")


    def print_structure(self):
        current_node = self.head
        if self.head is not None:
            while (current_node is not None):
                print(current_node.data)
                current_node = current_node.next
        else:
            print("Stack is empty")


new_node = Node("one")
new_stack = Stack(new_node)
new_stack.push("two")
new_stack.push("three")
new_stack.push("four")
new_stack.push("five")

print("New stack with 5 nodes.")
new_stack.print_structure()

new_stack.pop()
new_stack.pop()
new_stack.pop()
new_stack.pop()

new_stack.pop() #this must print "empty stack" message

new_stack.print_structure()#doesn't print an empty stack but a message