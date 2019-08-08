#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdint.h>

void *mallocc(size_t size) {
    void *ptr = malloc(size);
    if(ptr == NULL) {
        exit(EXIT_FAILURE);
    }
    return ptr;
}

typedef struct Node {
    int value;
    struct Node *xorAdress;
} Node;

Node *xorNodeAdresses(Node *a, Node *b) {
    return (Node *)((uintptr_t)a ^ (uintptr_t)b);
}

Node *add(Node *firstNode, int value) {
    Node *newNode = mallocc(sizeof(Node *));
    if(firstNode  != NULL) {
        (*firstNode).xorAdress = xorNodeAdresses(newNode, (*firstNode).xorAdress);
    }

    (*newNode).xorAdress = firstNode;
    (*newNode).value = value;
    return newNode;
}

Node *get(Node *firstNode, int index) {
    Node *prevNode = NULL;
    Node *ptr = firstNode;
    while(index--) {
        Node *nextNode = xorNodeAdresses((*ptr).xorAdress, prevNode);
        prevNode = ptr;
        ptr = nextNode;
    }
    return ptr;
}

int main() {
    Node *firstNode = NULL;
    for(int i=5; i>0; i--) {
        firstNode = add(firstNode, i);
    }

    printf("%d", (*get(firstNode, 0)).value);

    return EXIT_SUCCESS;
}