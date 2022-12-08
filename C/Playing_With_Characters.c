#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    char ch;
    scanf("%c", &ch);
  
    printf("%c", ch);
    printf("\n");
  
    char s1[100];
  
    fgets(s1, 100, stdin);
    gets(s1);
    printf("%s", s1);
    
    printf("\n");
    char s2[100];
    scanf("%[^\n]", s2);
    
    printf("%s", s2);
    return 0;
}
