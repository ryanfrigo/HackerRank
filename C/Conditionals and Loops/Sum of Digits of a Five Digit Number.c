#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    char a, b, c, d, e;
    scanf("%c%c%c%c%c", &a, &b, &c, &d, &e);
    printf("%d\n", (a - '0') + (b - '0') + (c - '0') + (d - '0') + (e - '0'));
    return (0);
}

