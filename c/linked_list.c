#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

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

bool list_push_front(LinkedList *list, item_type data) {
    if (list == NULL)
	return false;
    Node* new_node = create_node(data);
    if (new_node == NULL)
	return false;
    if (list->head == NULL) {
	list->head = new_node;
	list->tail = new_node;
    } else {
	new_node->next = list->head;
	list->head = new_node;
    }
    list->size++;
    return true;
}

bool list_append(LinkedList *list, item_type data) {
    if (list == NULL)
	return false;
    Node *new_node = create_node(data);
    if (new_node == NULL)
	return false;
    if (list->head == NULL) {
	list->head = new_node;
        list->tail = new_node;
    } else {
	list->tail->next = new_node;
        list->tail = new_node;
    }
    list->size++;
    return true;
}

bool list_pop_front(LinkedList *list, item_type *result) {
    if (list == NULL || list->head == NULL) {
	return false;
    }
    Node *temp = list->head;
    *result = temp->data;

    list->head = list->head->next;

    if (list->head == NULL) {
	list->tail = NULL;
    }

    free(temp);
    list->size--;
    return true;
}

int main() {
    printf("Creating list...\n");
    LinkedList *mylist = list_create();
    list_append(mylist, 10);
    list_append(mylist, 20);
    list_append(mylist, 30);
    list_print(mylist);
    printf("Popping front...\n");
    item_type popped_val;
    if (list_pop_front(mylist, &popped_val)) {
	printf("Popped: %d\n", popped_val);
    }      
    list_free(mylist);
    return 0;
}
