void postOrder(Node *root) {
        if(root != NULL){
            postOrder(root->left);
            postOrder(root->right);
            cout<<root->data<<" ";
        }
    }
