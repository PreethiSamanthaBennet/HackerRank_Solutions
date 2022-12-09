static SinglyLinkedListNode insertNodeAtTail(SinglyLinkedListNode head, int data) {
        SinglyLinkedListNode new_node = new SinglyLinkedListNode(data);
        
        if(head == null){
            head = new_node;
            return head;
        }
        
        SinglyLinkedListNode curr_node = head;
        while(curr_node.next != null){
            curr_node = curr_node.next;
        }
        curr_node.next = new_node;
        return head;
    }
