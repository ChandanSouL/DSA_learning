#1---->2---->3---->4
#to add a new node at the end of linked last
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
def addNodeAtBegining(head,new_data):
    new_node = Node(new_data)
    new_node.next = head
    return new_node

def addNodeAtGivenNode(head,new_data,key):
    curr = head
    while curr is not None:
        if curr.data == key:
            break
        curr = curr.next

        if curr is None:
            return head
    
    new_node = Node(new_data)
    new_node.curr = curr.next
    curr.next = new_node
    return head

def addNodeAtEnd(head,new_data):
    new_node = Node(new_data)
    if head is None:
        return new_node
    last = head
    while last.next:
        last = last.next
    last.next = new_node
    return head

def addNodeAtPosition(new_data,pos,head):
    new_node = Node(new_data)
    if pos ==1:
        new_node.next = head
        head = new_node
        return head
    current = head
    for i in range(1, pos - 1):
        if current is None:
            break
        current = current.next

    # If the position is out of bounds
    if current is None:
        return head

    new_node.next = current.next
    current.next = new_node
    return head

#reversing a linked list
def reverselinkedlist(head):
    # Initialize three pointers: curr, prev and next
    curr = head
    prev = None
    # Traverse all the nodes of Linked List
    while curr is not None:
        # Store next with curr
        next_node = curr.next
        # Reverse current node's next pointer
        curr.next = prev
        # Move pointers one position ahead
        prev = curr
        curr = next_node
    # Return the head of reversed linked list
    return prev

#Reverse a linked list by Recursion
def recurssionLinkedlist(head):
    if head is None and head.next is None:
        return head
    rest = recurssionLinkedlist(head.next)
    head.next.next = head
    head.next = None

    return rest
    