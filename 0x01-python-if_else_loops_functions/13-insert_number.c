#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - insert a node
 * @head: a node
 * @number: number to insert
 * Return: a linked list
**/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode;
	listint_t *nextnode;
	listint_t *tmpnode;

	newnode = malloc(sizeof(listint_t));
	tmpnode = *head;
	nextnode = tmpnode->next;

	while (nextnode->next != NULL)
	{
		if (nextnode->n > number)
		{
			tmpnode->next = newnode;
			newnode->next = nextnode;
			newnode->n = number;
			break;
		}
		else
		{
			tmpnode = tmpnode->next;
			nextnode = nextnode->next;
		}
	}
	return(*head);
}


