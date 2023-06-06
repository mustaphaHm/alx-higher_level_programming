#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - function that insert a number into a sorted linked list
 * @head: linked list
 * @number: the number to insert
 * Return: the address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *list, *new_node;

	list = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (list == NULL || list->n >= number)
	{
		new_node->next = list;
		*head = new_node;
		return (new_node);
	}

	while (list && list->next && list->next->n < number)
		list = list->next;

	new_node->next = list->next;
	list->next = new_node;

	return (new_node);
}
