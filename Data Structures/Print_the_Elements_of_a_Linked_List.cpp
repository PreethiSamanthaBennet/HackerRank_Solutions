void printLinkedList(SinglyLinkedListNode* n) {
    while(n != NULL){
        cout<<n->data<<" "<<endl;
        n = n->next;
    }
}
