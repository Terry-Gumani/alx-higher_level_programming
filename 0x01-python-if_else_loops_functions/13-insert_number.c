#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} listint_t;

listint_t* createNode(int number) {
    listint_t* newNode = (listint_t*)malloc(sizeof(listint_t));
    if (newNode == NULL) {
        printf("Memory allocation failed.\n");
        return NULL;
    }
    newNode->data = number;
    newNode->next = NULL;
    return newNode;
}

listint_t* insert_node(listint_t** head, int number) {
    listint_t* newNode = createNode(number);
    if (newNode == NULL) {
        return NULL;
    }
    
    if (*head == NULL || number < (*head)->data) {
        newNode->next = *head;
        *head = newNode;
    } else {
        listint_t* current = *head;
        while (current->next != NULL && number > current->next->data) {
            current = current->next;
        }
        newNode->next = current->next;
        current->next = newNode;
    }
    
    return newNode;
}

void printList(listint_t* head) {
    listint_t* current = head;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}

int main() {
    listint_t* head = NULL;
    
    insert_node(&head, 5);
    insert_node(&head, 10);
    insert_node(&head, 15);
    
    printf("Original list: ");
    printList(head);
    
    listint_t* newNode = insert_node(&head, 12);
    if (newNode != NULL) {
        printf("New node inserted: %d\n", newNode->data);
        printf("Updated list: ");
        printList(head);
    } else {
        printf("Failed to insert new node.\n");
    }
    
    return 0;
}

