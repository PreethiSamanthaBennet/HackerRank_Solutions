def insertNodeAtPosition(llist, data, position):
    node = SinglyLinkedListNode(data)

    if llist == None:
        llist = node

    else:
        temp = llist
        count = 1

        while temp != None and count < position:
            temp = temp.next
            count += 1

        node.next = temp.next
        temp.next = node
    return llist
