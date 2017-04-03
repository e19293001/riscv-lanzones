#ifndef BST_H
struct mem {
  unsigned int address;
  unsigned int data;
};

typedef struct mem mem;  

struct node {
  mem data;
  struct node* left;
  struct node* right;
};

typedef struct node node;

node *bst_new(mem memdata);
node *bst_insert(node *n, mem memdata);
unsigned int bst_search(node *n, mem memdata);
void bst_free(node *n);

#ifdef DEBUG_BST
void testsearch(node *bst, mem memdata);
#endif
#endif
