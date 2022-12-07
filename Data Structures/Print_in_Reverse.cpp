void reversePrint(SinglyLinkedListNode* llist) {
    if(!llist) return;
    
    reversePrint(llist->next);
    cout<<llist->data<<endl;
}
