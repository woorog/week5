//////////////////////////////////////////////////////////////////////////////////

/* CE1007/CZ1007 Data Structures
Lab Test: Section F - Binary Search Trees Questions
Purpose: Implementing the required functions for Question 2 */

//////////////////////////////////////////////////////////////////////////////////

#include <stdio.h>
#include <stdlib.h>

//////////////////////////////////////////////////////////////////////////////////

typedef struct _bstnode {
	int item;
	struct _bstnode* left;
	struct _bstnode* right;
} BSTNode;   // You should not change the definition of BSTNode

typedef struct _stackNode {
	BSTNode* data;
	struct _stackNode* next;
}StackNode; // You should not change the definition of StackNode

typedef struct _stack
{
	StackNode* top;
}Stack; // You should not change the definition of Stack

///////////////////////// function prototypes ////////////////////////////////////

// You should not change the prototypes of these functions
void inOrderTraversal(BSTNode* node);

void insertBSTNode(BSTNode** node, int value);

void push(Stack* stack, BSTNode* node);
BSTNode* pop(Stack* s);
BSTNode* peek(Stack* s);
int isEmpty(Stack* s);
void removeAll(BSTNode** node);

///////////////////////////// main() /////////////////////////////////////////////

int main()
{
	int c, i;
	c = 1;

	//Initialize the Binary Search Tree as an empty Binary Search Tree
	BSTNode* root;
	root = NULL;

	printf("1: Insert an integer into the binary search tree;\n");
	printf("2: Print the in-order traversal of the binary search tree;\n");
	printf("0: Quit;\n");


	while (c != 0)
	{
		printf("Please input your choice(1/2/0): ");
		scanf_s("%d", &c);

		switch (c)
		{
		case 1:
			printf("Input an integer that you want to insert into the Binary Search Tree: ");
			scanf_s("%d", &i);
			insertBSTNode(&root, i);
			break;
		case 2:
			printf("The resulting in-order traversal of the binary search tree is: ");
			inOrderTraversal(root); // You need to code this function
			printf("\n");
			removeAll(&root);
			break;
		case 0:
			removeAll(&root);
			break;
		default:
			printf("Choice unknown;\n");
			break;
		}

	}

	return 0;
}

//////////////////////////////////////////////////////////////////////////////////

void inOrderTraversal(BSTNode* root)
{
	if (root == NULL)
		return;

	Stack tree_s;
	BSTNode* cur;

	tree_s.top = NULL;
	cur = root;

	while (1)
	{
		if (cur != NULL) {
			push(&tree_s, cur);
			cur = cur->left;
		}
		else {
			if (!isEmpty(&tree_s)) {
				cur = pop(&tree_s);
				printf("%d ", cur->item);
				cur = cur->right;
			}
			else
				break;
		}
	}
}

//void inOrderTraversal(BSTNode* root)
//{
//	if (root == NULL)
//		return;
//
//	BSTNode* cur = root;
//	Stack tree_s;
//	tree_s.top = NULL;
//	push(&tree_s, root);
//
//	while (!isEmpty(&tree_s)) {
//		// 현재 시점에서 왼쪽 내려가면서 푸시
//		while (cur->left != NULL) {
//			push(&tree_s, cur->left);
//			cur = cur->left;
//		}
//		// 오른쪽 자식이 있는 노드까지 올라가면서 팝&출력
//		while (cur->right == NULL) {
//			cur = pop(&tree_s);
//
//			// 탈출조건
//			if (cur == NULL)
//				return;
//
//			printf("%d ", cur->item);
//		}
//		// 오른쪽 자식 푸시 [예외처리) 루트가 첫 pop 값인 경우]
//		if (cur != root) {
//			push(&tree_s, cur->right);
//			cur = cur->right;
//		}
//		// 예외처리) 오른쪽으로만 펴진 가지일때
//		while (cur->right != NULL && cur->left == NULL) {
//			printf("%d ", pop(&tree_s)->item);
//			push(&tree_s, cur->right);
//			cur = cur->right;
//		}
//	}
//
//	if (!isEmpty(&tree_s)) {
//		BSTNode* remain = peek(&tree_s);
//		removeAll(&remain);
//	}
//}

///////////////////////////////////////////////////////////////////////////////

void insertBSTNode(BSTNode** node, int value) {
	if (*node == NULL)
	{
		*node = malloc(sizeof(BSTNode));

		if (*node != NULL) {
			(*node)->item = value;
			(*node)->left = NULL;
			(*node)->right = NULL;
		}
	}
	else
	{
		if (value < (*node)->item)
		{
			insertBSTNode(&((*node)->left), value);
		}
		else if (value > (*node)->item)
		{
			insertBSTNode(&((*node)->right), value);
		}
		else
			return;
	}
}

//////////////////////////////////////////////////////////////////////////////////

void push(Stack* stack, BSTNode* node)
{
	StackNode* temp;

	temp = malloc(sizeof(StackNode));

	if (temp == NULL)
		return;
	temp->data = node;

	if (stack->top == NULL)
	{
		stack->top = temp;
		temp->next = NULL;
	}
	else
	{
		temp->next = stack->top;
		stack->top = temp;
	}
}

BSTNode* pop(Stack* s)
{
	StackNode* temp, * t;
	BSTNode* ptr;
	ptr = NULL;

	t = s->top;
	if (t != NULL)
	{
		temp = t->next;
		ptr = t->data;

		s->top = temp;
		free(t);
		t = NULL;
	}

	return ptr;
}

BSTNode* peek(Stack* s)
{
	StackNode* temp;
	temp = s->top;
	if (temp != NULL)
		return temp->data;
	else
		return NULL;
}

int isEmpty(Stack* s)
{
	if (s->top == NULL)
		return 1;
	else
		return 0;
}


void removeAll(BSTNode** node)
{
	if (*node != NULL)
	{
		removeAll(&((*node)->left));
		removeAll(&((*node)->right));
		free(*node);
		*node = NULL;
	}
}
