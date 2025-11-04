#include <stdio.h>
#include <stdlib.h>

typedef int item_type;

typedef struct Node {
    item_type data;
    struct Node *next;
} Node;

typedef struct LinkedList {
    Node *head;
    Node *tail;
    size_t size;
} LinkedList;

static Node* create_node(item_type data) {
    Node *new_node = (Node *)malloc(sizeof(Node));
    if (new_node == NULL) {
	return NULL;
    }
    new_node->data = data;
    new_node->next = NULL;
    return new_node;
}

LinkedList* list_create() {
    LinkedList *list = (LinkedList *)malloc(sizeof(LinkedList));
    if (list == NULL) {
	return NULL;
    }
    list->head = NULL;
    list->tail = NULL;
    list->size = 0;
    return list;
}

void list_free(LinkedList *list) {
    if (list == NULL) return;
    Node* current = list->head;
    Node *next;
    while (current != NULL) {
	next = current->next;
        free(current);
	current = next;
    }
    free(list);
}

void list_print(const LinkedList *list) {
    if (list == NULL) {
	printf("List is (null)\n");
    }
    Node *current = list->head;
    printf("List (size %zu): HEAD -> ", list->size);
    while (current != NULL) {
	printf("[%d] -> ", current->data);
	current = current->next;
    }
    printf("NULL\n");
}

int main()
{
    return 0;
}
