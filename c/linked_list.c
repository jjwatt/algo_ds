#include <stdio.h>
#include <stdlib.h>

typedef int item_type;

typedef struct Node {
    item_type item;
    struct Node *next;
} Node;

void append(Node *head, item_type val)
{
    Node *current = head;
    while(current->next != NULL) {
	current = current->next;
    }
    current->next = (Node*) malloc(sizeof(Node));
    current->next->item = val;
    current->next->next = NULL;
}

Node* list(item_type val)
{
    Node *head = (Node*) malloc(sizeof(Node));
    head->item = val;
    head->next = NULL;
    return head;
}

void print_list(Node* head)
{
    Node* current = head;
    while(current != NULL) {
	printf("%d\n", current->item);
	current = current->next;
    }
}

item_type pop_last(Node* head)
{
    Node* current = NULL;
    item_type retval = {0};
    if (head->next == NULL) {
	retval = head->item;
	free(head);
	return retval;
    }
    current = head;
    while (current->next->next != NULL) {
	current = current->next;
    }
    retval = current->next->item;
    free(current->next);
    current->next = NULL;
    return retval;
}

int main()
{
    Node* llist = list(10);
    append(llist, 20);
    append(llist, 30);
    print_list(llist);
    printf("%d\n", pop_last(llist));
    printf("%d\n", pop_last(llist));
    printf("%d\n", pop_last(llist));
}
