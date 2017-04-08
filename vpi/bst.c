#include <bst.h>
#include <stdlib.h>
#include <stdio.h>

node *bst_new(mem memdata) {
  node* nd = malloc(sizeof(memdata));
  nd->data = memdata;
  nd->left = NULL;
  nd->right = NULL;
  return nd;
}

void bst_traverse(node *n) {
  if (n == NULL) {
    //printf("[ bst_traverse ] returning\n");
  }
  else {
    bst_traverse(n->left);
    printf("[ bst_traverse ] address: %08X data: %08X\n", n->data.address, n->data.data);
    bst_traverse(n->right);
  }
}

node *bst_insert(node *n, mem memdata) {
  if (n == NULL) {
    //printf("[ bst_insert ] n is NULL creating new\n");
    node *nd = bst_new(memdata);
    return nd;
  }
  else {
    if (memdata.address <= n->data.address) {
      //printf("[ bst_insert ] [ going to LEFT ] memdata.address: %0d\n", memdata.address);
      n->left = bst_insert(n->left, memdata);
    }
    else {
      //printf("[ bst_insert ] [ going to RIGHT ] memdata.address: %0d\n", memdata.address);
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

unsigned int bst_search(node *n, mem memdata) {
  if (n == NULL) {
    return 0;
  }
  if (memdata.address == n->data.address) {
    return n->data.data;
  }
  else if (memdata.address < n->data.address) {
    bst_search(n->left, memdata);
  }
  else if (memdata.address > n->data.address) {
    bst_search(n->right, memdata);
  }
//  printf("searching for mem.address: %08X\n", memdata.address);
////  if (n == NULL || memdata.address == n->data.address) {
//  if (n == NULL) {
////  if (memdata.address == n->data.address) {
////    printf("returning data: %0d\n", n->data.data);
////    return n->data.data;
//    return 0;
//  }
//  else if (memdata.address < n->data.address) {
//    bst_search(n->left, memdata);
//  }
//  else if (memdata.address > n->data.address) {
//    bst_search(n->right, memdata);
//  }
//  else {
//    printf("FOUND %08X\n", n->data.data);
//    return n->data.data;
////    return 0;
//  }
//  return 0;
}

#ifdef DEBUG_BST
void testsearch(node *bst, mem memdata) {
  printf("testing search...\n");
  printf("                  address: %08X\n", memdata.address);
  printf("                  data: %08X\n", bst_search(bst,memdata));
//  if (bst_search(bst,memdata) == 1) {
//    printf("%0d found\n", memdata.address);
//  }
//  else {
//    printf("%0d not found\n", memdata.address);
//  }
}

void testbst1() {
  node *bst;
  mem memdata;
  printf("-------------------- start --------------------\n");
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
  bst_traverse(bst);
  bst_free(bst);
  printf("-------------------- end --------------------\n");
}

void testbst2() {
  node *bst = NULL;
  mem memdata;
  printf("-------------------- start --------------------\n");
  memdata.address = 0;
  memdata.data = 0xAAA;
  bst = bst_insert(bst,memdata);
  bst_traverse(bst);
  memdata.address = 1;
  memdata.data = 0xBBB;
  bst = bst_insert(bst,memdata);
  bst_traverse(bst);
  //printf("bst->left->data.address: %0d\n", bst->left->data.address);
  memdata.address = 2;
  memdata.data = 0xCCC;
  bst = bst_insert(bst,memdata);
  bst_traverse(bst);
  memdata.address = 0;
  testsearch(bst,memdata);
  memdata.address = 1;
  testsearch(bst,memdata);
  memdata.address = 2;
  testsearch(bst,memdata);
  
  bst_traverse(bst);
  bst_free(bst);
  printf("-------------------- end --------------------\n");
}

int main() {
  testbst1();
  testbst2();
  return 0;  
}
#endif
