/* Dynamic Array Backed Linked List */
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int data;
    int next;
} Node;

typedef struct {
    Node* nodes;
    int capacity;
    int size;
    int head;
    int free_list;
} LinkedList;

LinkedList* list_create(int initial_capacity) {
    LinkedList* list = malloc(sizeof(LinkedList));
    list->nodes = malloc(sizeof(initial_capacity * sizeof(Node)));
    list->capacity = initial_capacity;
    list->size = 0;
    list->head = -1;
    list->free_list = -1;
    return list;
}

void list_resize(LinkedList* list) {
    int new_capacity = list->capacity * 2;
    list->nodes = realloc(list->nodes, new_capacity * sizeof(Node));
    list->capacity = new_capacity;
}

int list_allocate_node(LinkedList* list) {
    int index;

    // Use free list if available.
    if (list->free_list != -1) {
        index = list->free_list;
        list->free_list = list->nodes[index].next;
        return index;
    }
    // Otherwise use next available slot.
    if (list->size >= list->capacity) {
        list_resize(list);
    }
    index = list->size;
    list->size++;
    return index;
}

void list_push_front(LinkedList* list, int data) {
    int index = list_allocate_node(list);
    list->nodes[index].data = data;
    list->nodes[index].next = list->head;
    list->head = index;
}

void list_push_back(LinkedList* list, int data) {
    int index = list_allocate_node(list);
    list->nodes[index].data = data;
    list->nodes[index].next = -1;

    if (list->head == -1) {
        list->head = index;
    } else {
        int curr = list->head;
        while (list->nodes[curr].next != -1) {
            curr = list->nodes[curr].next;
        }
        list->nodes[curr].next = index;
    }
}

int list_pop_front(LinkedList* list) {
    if (list->head == -1) {
        fprintf(stderr, "ERROR: List is empty.\n");
        exit(1);
    }
    int old_head = list->head;
    int data = list->nodes[old_head].data;
    list->head = list->nodes[old_head].next;

    // Add to free list.
    list->nodes[old_head].next = list->free_list;
    list->free_list = old_head;
    return data;
}

void list_free(LinkedList* list) {
    free(list->nodes);
    free(list);
}

void list_print(LinkedList* list) {
    int curr = list->head;
    printf("List: ");
    while (curr != -1) {
        printf("%d -> ", list->nodes[curr].data);
        curr = list->nodes[curr].next;
    }
    printf("NULL\n");
}

int main() {
    LinkedList* list = list_create(4);
    list_push_front(list, 3);
    list_push_front(list, 2);
    list_push_front(list, 1);

    list_print(list);
}
