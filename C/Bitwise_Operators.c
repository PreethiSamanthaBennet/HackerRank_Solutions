#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void calculate_the_maximum(int n, int k) {
  int i, j, m1 = 0, m2 = 0, m3 = 0;

  for( i = 1; i <= n; i++){
      for(j = i+1; j <= n; j++){
          int and = i & j;
          int or = i | j;
          int xor = i ^ j;

          if(and < k && m1 < and)
              m1 = and;

          if(or < k && m2 < or)
              m2 = or;

          if(xor < k && m3 < xor)
              m3 = xor;
      }
  }
  printf("%d\n", m1);
  printf("%d\n", m2);
  printf("%d\n", m3);
}

int main() {
    int n, k;
    
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);

    return 0;

}
