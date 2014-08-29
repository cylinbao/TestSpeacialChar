#include "stdio.h"
#include "stdlib.h"

int main(int argc, char* argv[])
{
	int i;
	char *c;

	c = (char*) malloc(95);

	for(i=0; i<95; i++){
		c[i] = 32+i;
	}

	for(i=0; i<95; i++){
		printf("c[%d] = %c\n", i, c[i]);
	}

	return 0;
}
