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
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	if (*head == NULL)
	{
		*head = newnode;
		return (*head);
	}
	tmpnode = *head;
	if (tmpnode->next != NULL)
		nextnode = tmpnode->next;
	if (tmpnode->n > number)
	{
		newnode->next = *head;
		*head = newnode;
		return (*head);
	}
	while (nextnode->next != NULL)
	{
		if (nextnode->n > number)
		{
			tmpnode->next = newnode;
			newnode->next = nextnode;
			break;
		}
		else
		{
			tmpnode = tmpnode->next;
			nextnode = nextnode->next;
		}
	}
	if (nextnode->n < number)
		nextnode->next = newnode;
	return (*head);
}
