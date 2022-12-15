static SinglyLinkedListNode insertNodeAtHead(SinglyLinkedListNode llist, int data) {
        SinglyLinkedListNode new_node = new SinglyLinkedListNode(data);
        
        if(llist == null) return new_node;
        
        SinglyLinkedListNode temp = llist;
        
        llist = new_node;
        llist.next = temp;
        return llist;
    }
