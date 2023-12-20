from src.data_structures.linked_list import LinkedList, Node

llist = LinkedList()

for i in range(10):
    llist.append(Node(i))

for node in llist:
    print(f"Node type: {type(node)} Current node data = {node.data}")

head = llist.head
tail = llist.tail

print(f"LinkedList head data = {head.data}, LinkedList tail data = {tail.data}")
