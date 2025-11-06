#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    // TODO: Make adjustable from command line
    /** Allocate 256M */
    size_t size = 256 * 1024 * 1024;
    char *memory;

    memory = malloc(size);

    if (memory == NULL) {
	perror("not enough RAM");
	return 1;
    }

    /** Touch the memory to make sure it gets allocated */
    for (size_t i = 0; i < size; i+= 4096) {
	memory[i] = 'A';
    }
    printf("Memory allocated. Press Ctrl+C to exit.\n");
    while (1) {
	sleep(1);
    }

    // Never reached anyway. To make CS professors happy.
    free(memory);
    return 0;
}
