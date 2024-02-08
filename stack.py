class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:
     def __init__(self):
         self.top = None
         
     def push(self, data):
         new_node = Node(data)
         if self.top is None:
             self.top = new_node
         else:
             new_node.next = self.top
             self.top = new_node
             
     def pop(self):
         if self.top is None:
             return None
         else:
             popped = self.top.data
             self.top = self.top.next
             return popped
             
def reverse_string_using_stack(input_string):
    stack = Stack()
    for char in input_string:
        stack.push(char)
        
    reversing_input = ''
    while True:
        char = stack.pop()
        if char is None:
            break
        reversing_input += char
        
    return reversing_input
    
user_input = input("Enter a string: ")
reversing_input = reverse_string_using_stack(user_input)
 print(" ", reversing_input)