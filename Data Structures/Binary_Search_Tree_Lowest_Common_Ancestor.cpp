Node *lca(Node *root, int v1,int v2) {
        if(root->data<v1 && root->data<v2){
            return lca(root->right, v1, v2);
        }
        
        else if(root->data>v1 && root->data>v2){
            return lca(root->left, v1, v2);
        }
        
        else{
            return root;
        }
    }
