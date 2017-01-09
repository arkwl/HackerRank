#include <stdio.h>
#include <string.h>
#include <math.h>
void displayPathtoPrincess(int n, char grid[101][101]){
  int i, j, up, left;
  short mario[2], princess[2];

  /* find mario & princess */
  for(i = 0; i < n; ++i) {
    for(j = 0; j < n; ++j) {
      if (grid[i][j] == 'm') {
        mario[0] = i;
        mario[1] = j;
      }
      if (grid[i][j] == 'p') {
        princess[0] = i;
        princess[1] = j;
      }
    }
  }

  if ((up = princess[0] - mario[0]) < 0) {
    for(; up < 0; ++up)
      printf("UP\n");
  } else {
    for(; up > 0; --up)
      printf("DOWN\n");
  }

  if ((left = princess[1] - mario[1]) < 0) {
    for(; left < 0; ++left)
      printf("LEFT\n");
  } else {
    for(; left > 0; --left)
      printf("RIGHT\n");
  }
}

int main(void) {

    int m;
    scanf("%d", &m);
    char grid[101][101]={};
    char line[101];

    for(int i=0; i<m; i++) {
        scanf("%s", line);
        strcpy(grid[i], line);
    }
    displayPathtoPrincess(m,grid);
    return 0;
}
