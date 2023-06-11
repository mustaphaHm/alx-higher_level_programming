#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * find_mid - function to fin the midlle of a linked list
 * @head: pointer to the head list
 * Return: listint_t - reversed list
*/
listint_t *find_mid(listint_t *head)
{
	listint_t *fast;
	listint_t *slow;

	if (head == NULL)
	{
		return (NULL);
	}

	fast = head;
	slow = head;

	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast->next != NULL)
	{ /* if the linked list is even*/
		slow = slow->next;
	}

	return (slow);
}
/**
 * reverse_list - function to fin the midlle of a linked list
 * @head: pointer to the head list
 * Return: listint_t - reversed list
*/
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;  /* Store the next node*/
		current->next = prev;  /* Reverse the pointer direction*/

		prev = current;/* Move prev and current one step forward*/
		current = next;
	}

	return (prev);  /* Return the new head of the reversed list*/
}
/**
 * is_palindrome - check if a linked list is palindrome
 * @head: pointer to head of list
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *middle = find_mid(*head);
	listint_t *reversed = reverse_list(middle->next);
	listint_t *current = *head;
	listint_t *reversedCurrent = reversed;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
	{
		return (1);  /* if empty or single list , it's a  palindrome*/
	}

	while (reversedCurrent != NULL)
	{
		if (current->n != reversedCurrent->n)
		{
			return (0);  /* Mismatch found, not a palindrome*/
		}
		current = current->next;
		reversedCurrent = reversedCurrent->next;
	}

	return (1);  /* No mismatches found, it is a palindrome*/
}
