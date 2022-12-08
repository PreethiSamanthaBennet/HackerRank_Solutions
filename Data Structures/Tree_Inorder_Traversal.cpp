void inOrder(Node *n) {
        if(n != NULL){
            inOrder(n->left);
            cout<<n->data<<" ";
            inOrder(n->right);
        }
    }
