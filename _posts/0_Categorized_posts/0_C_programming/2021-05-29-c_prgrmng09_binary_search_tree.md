---
title: C - binary search tree를 구현해봤습니다. 
category: C_programming
tags: C programming C_programming tree bst binary_search_tree data_structure
---

## C - binary search tree를 구현해봤습니다 

- binary search tree를 구현해봤습니다.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct NODE {
    int value;
    struct NODE* left;
    struct NODE* right;
} NODE;

NODE* new_node(int value) {
    // 새로운 NODE memory를 확보하고 값을 넣어줘서 리턴.
    NODE* temp_node = (NODE*) malloc(sizeof(NODE) * 1);
    temp_node->value = value;
    temp_node->left = NULL;
    temp_node->right = NULL;
    return temp_node;
}

NODE* add_node(NODE* root_node, int value) {
    // root_node를 포함한 하위 node에 value를 넣어준다.
    if (root_node == NULL) {
        return new_node(value);
    } else {
        NODE* pointer = root_node;
        if (value < pointer->value) {
            pointer->left = add_node(pointer->left, value);
        } else if (pointer->value < value) {
            pointer->right = add_node(pointer->right, value);
        } else {
            printf("not unique \n");
        }
        return pointer;
    }
}

int get_height(NODE* root_node) {
    if (root_node == NULL) {
        return 0;
    } else {
        int left_tree_height = get_height(root_node->left);
        int right_tree_height = get_height(root_node->right);
        return left_tree_height > right_tree_height ? left_tree_height + 1 : right_tree_height + 1;
    }
}

NODE* find_node(NODE* root_node, int value) {
    // root_node의 하위 node들 중에 value를 값으로 가진 node를 찾아서 리턴함.
    NODE* pointer = root_node;
    if (root_node == NULL) {
        return NULL;
    } else {
        if (pointer->value == value) {
            return pointer;
        } else if (pointer->value < value) {
            return find_node(root_node->right, value);
        } else {
            return find_node(root_node->left, value);
        }
    }
}

void swap_node_value(NODE* node_a, NODE* node_b) {
    int temp_value;
    temp_value = node_a->value;
    node_a->value = node_b->value;
    node_b->value = temp_value;
}

NODE* delete_node(NODE* root_node, int value) {
    if (root_node == NULL) {
        return NULL;
    } else {
        if (root_node->value < value) {
            root_node->right = delete_node(root_node->right, value);
            return root_node;
        } else if (value < root_node->value) {
            root_node->left = delete_node(root_node->left, value);
            return root_node;
        } else {
            // value == root_node->value 
            NODE* left_child = root_node->left;
            NODE* right_child = root_node->right;
            if (left_child != NULL) {
                if (right_child != NULL) {
                    // both exist
                    swap_node_value(root_node, left_child);
                    root_node->left = delete_node(root_node->left, value);
                    return root_node;
                } else {
                    // left exists
                    return left_child;
                }
            } else {
                if (right_child != NULL) {
                    // right exist 
                    return right_child;
                } else {
                    // both not exists
                    return NULL;
                }
            }
        }
    }
}

int get_tree_size(NODE* root_node) {
    if (root_node == NULL) {
        return 0;
    } else {
        int left_tree_size = get_tree_size(root_node->left);
        int right_tree_size = get_tree_size(root_node->right);
        return 1 + left_tree_size + right_tree_size;
    }
}

void preorder(NODE* root_node) {
    if (root_node != NULL) {
        printf("%d ", root_node->value);
        preorder(root_node->left);
        preorder(root_node->right);
    }
}
void inorder(NODE* root_node) {
    if (root_node != NULL) {
        inorder(root_node->left);
        printf("%d ", root_node->value);
        inorder(root_node->right);
    }
}

void print_tree(NODE* root_node) {
    printf("== height: %d \n", get_height(root_node));
    printf("== tree size: %d \n", get_tree_size(root_node));
    printf("== preorder\n");
    preorder(root_node);
    printf("\n");
    printf("== inorder\n");
    inorder(root_node);
    printf("\n");
}

int main(void) {
    NODE* global_root_node = NULL;
    global_root_node = add_node(global_root_node, 2);
    global_root_node = add_node(global_root_node, 1);
    global_root_node = add_node(global_root_node, 3);
    print_tree(global_root_node);
    global_root_node = delete_node(global_root_node, 2);
    global_root_node = delete_node(global_root_node, 1);
    global_root_node = delete_node(global_root_node, 3);
    global_root_node = delete_node(global_root_node, 3);
    print_tree(global_root_node);
    global_root_node = add_node(global_root_node, 3);
    print_tree(global_root_node);
}
```
