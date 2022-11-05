#include <stdio.h>
#include <stdlib.h>
  
int main()
{
    FILE *fptr;
  
    char c;
  
    fptr = fopen("/flag.txt","r");
    if (fptr == NULL)
    {
        printf("Cannot open file \n");
        exit(0);
    }

    c = fgetc(fptr);
    while (c != EOF)
    {
        printf ("%c", c);
        c = fgetc(fptr);
    }
  
    fclose(fptr);
    return 0;

}