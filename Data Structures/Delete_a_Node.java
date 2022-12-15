class Result {

    public static SinglyLinkedListNode deleteNode(SinglyLinkedListNode llist, int position) {

        if(llist == null) return llist;

        if(position == 0) return llist.next;

        int counter = 0;
        SinglyLinkedListNode curr_node = llist;
        
        while(counter < position-1){
            curr_node = curr_node.next;
            counter++;
        }
        
        curr_node.next = curr_node.next.next;
        return llist;
    }

}
