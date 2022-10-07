class node:
    def __init__(self,val):
        self.val =val
        self.next = None
        self.prev = None


dlist = node(1)
head = dlist
tail = dlist

# traverse from front
def front_traversal(head):
    root = head
    while root :
        print(root.val,end='--->')
        root =root.next
    print('\n')

# front_traversal(head)

def back_traversal(tail):
    root =tail
    while root:
        print(root.val, end='--->')
        root =root.prev
    print('\n')

back_traversal(tail)

def front_insertion(head,val):
    newnode = node(val)
    head.prev = newnode
    newnode.next =head
    return newnode

head = front_insertion(head,20)
head = front_insertion(head,30)
head = front_insertion(head,40)

front_traversal(head)