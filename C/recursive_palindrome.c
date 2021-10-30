#include <stdio.h>
#include <stdlib.h>
#define MAX 500

int find_tam(char *string)
{
	int per = 0;
	
	while(string[per] != '\0')
	{
		per++;
	}
	return per;
}
int palindrome_check(char *string, int index, int ini)
{
	if (index >= 0)
	{
		if (string[ini] != string[index])
			return 0;
		else
		{
			int m = index - 1;
			int n = ini + 1; 
			return (palindrome_check(string, m, n));
		}
	}
	return 1;

}
int main()
{
	char *reader;
	reader = malloc(MAX*sizeof(char));
	scanf("%s",reader);
	int tam = find_tam(reader);
	int tr = palindrome_check(reader,tam-1,0);
	if (tr)
		printf("PALINDROME\n");
	else
		printf("NOT PALINDROME\n");
	return 0;
}