void reorder(Node **head, Node *right){
    if(right == NULL){
        return;
    }
    
    reorder(head, right->next);
    if((*head)->next== NULL){
        return;
    }
    if((*head) == right || (*head)->next == right){
        if((*head)->next == right){
             (*head) = (*head)->next;
        }
        (*head)->next = NULL;
        return;
    }
   
    Node*temp = (*head)->next;
    (*head)->next = right;
    right->next = temp;
    (*head) = temp;
}

void reorderList(Node* head) {
    reorder(&head, head->next);
}