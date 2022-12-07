SinglyLinkedListNode* reverse(SinglyLinkedListNode* llist) {
    SinglyLinkedListNode*prev = NULL;
    SinglyLinkedListNode*current = llist;
    SinglyLinkedListNode*next;
    
    while(current != NULL){
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    llist = prev;
    return llist;
}
