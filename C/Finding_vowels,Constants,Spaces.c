#include <stdio.h>
void main() 
{
    char line[100];
    int i, v=0, con=0, sp=0;
    printf("Enter a sentence:\n");
    gets(line);
    for (i=0; line[i]!='\0' ;++i) 
    {
        if (line[i] == 'a' || line[i] == 'e' || line[i] == 'i' ||
            line[i] == 'o' || line[i] == 'u' || line[i] == 'A' ||
            line[i] == 'E' || line[i] == 'I' || line[i] == 'O' ||
            line[i] == 'U')
           {
            ++v;
           } 
        else if ((line[i] >= 'a' && line[i] <= 'z') || (line[i] >= 'A' && line[i] <= 'Z'))
        {
            ++con;
        }
        else if (line[i] == ' ')
        {
            ++sp;
        }
    }
    printf("\nNumber of Vowels: %d", v);
    printf("\n\nNumber of Constants: %d", con);
    printf("\n\nNumber of spaces: %d", sp);
    return 0;
}
