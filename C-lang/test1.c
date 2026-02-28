#include <stdio.h>

int main()
{
    int i = 5;
    int* j = &i;

    char a = 'x';
    char* b = &a;

    printf("%d\n%p\n%c\n%p\n", i, j, a, b);
    printf("%c\n", *(b));
    printf("%d\n", *(b));
}