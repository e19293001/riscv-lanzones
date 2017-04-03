#include <bst.h>
#include <stdlib.h>
#include <stdio.h>

node *bst_new(mem memdata) {
  node* nd = malloc(sizeof(memdata));
  nd->data = memdata;
  nd->left = NULL;
  nd->right = NULL;
}

node *bst_insert(node *n, mem memdata) {
  if (n == NULL) {
    node *nd = bst_new(memdata);
    return nd;
  }
  else {
    if (memdata.address <= n->data.address) {
      n->left = bst_insert(n->left, memdata);
    }
    else {
      n->right = bst_insert(n->right, memdata);
    }
    return n;
  }
}

void bst_free(node *n) {
  if (n->left != NULL) {
    bst_free(n->left);
  }
  if (n->right != NULL) {
    bst_free(n->right);
  }
  free(n);
}

int bst_search(node *n, mem memdata) {
  if (n == NULL) {
    return 0;
  }
  else {
    if (memdata.address < n->data.address) {
      bst_search(n->left, memdata);
    }
    else if (memdata.address > n->data.address) {
      bst_search(n->right, memdata);
    }
    else {
      return 1;
    }
  }
}

#ifdef DEBUG_BST
void testsearch(node *bst, mem memdata) {
  if (bst_search(bst,memdata) == 1) {
    printf("%0d found\n", memdata.address);
  }
  else {
    printf("%0d not found\n", memdata.address);
  }
}

int main() {
  node *bst;
  mem memdata;
  memdata.address = 10;
  memdata.data = 0xAAA;
  bst = bst_new(memdata);
  printf("bst->data.address: %0d\n", bst->data.address);
  memdata.address = 9;
  memdata.data = 0xBBB;
  bst = bst_insert(bst,memdata);
  printf("bst->left->data.address: %0d\n", bst->left->data.address);
  bst = bst_insert(bst,memdata);
  memdata.address = 11;
  memdata.data = 0xCCC;
  bst = bst_insert(bst,memdata);
  printf("bst->left->data.address: %0d\n", bst->left->data.address);
  bst = bst_insert(bst,memdata);
  memdata.address = 9;
  memdata.data = 0xBBB;
  testsearch(bst,memdata);
  memdata.address = 10;
  memdata.data = 0xBBB;
  testsearch(bst,memdata);
  memdata.address = 11;
  memdata.data = 0xBBB;
  testsearch(bst,memdata);
  memdata.address = 12;
  memdata.data = 0xBBB;
  testsearch(bst,memdata);
  bst_free(bst);
  return 0;  
}
#endif