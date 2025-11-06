#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <stdint.h>
#include <unistd.h>

int main(int argc, char *argv[]) {

    /** Default size to allocate set to 0*/
    size_t size_mb = 0;

    if (argc > 1) {
	if (strcmp(argv[1], "-h") == 0 || strcmp(argv[1], "--help") == 0) {
	    printf("Usage: %s [size in megabytes]\n", argv[0]);
	    printf(" Allocates the specified amount of memory in Megabytes\n");
	    printf(" And holds it until program is exited by Ctrl-C or SIGTERM");
	    printf("Example: %s 1024 (allocates 1024 MB or 1GB)\n", argv[0]);
	    return 0;
	}

	/* Convert the argument to an integer */
	char *endptr;
	size_mb = strtol(argv[1], &endptr, 10);

	/* Error handling for strtol */
	if (*endptr != '\0') {
	    fprintf(stderr, "Error Invalid size argument '%s'. Must be an integer\n", argv[1]);
	    return 1;
	}
	if (errno == ERANGE) {
	    fprintf(stderr, "Error: Size argument '%s' is out of range.\n", argv[1]);
	    return 1;
	}
	if (size_mb <= 0) {
	    fprintf(stderr, "Error: Size must be greater than 0.\n");
	    return 1;
	}
    } else {
	fprintf(stderr, "Error: Missing size argument.");
	return 1;
    }

    size_t size_bytes = size_mb * 1024 * 1024;

    // Check for overflow
    if (size_mb * 1024 * 1024 > SIZE_MAX) {
	fprintf(stderr, "Error: Requested size is too large (overflow).\n");
	return 1;
    }

    char* memory = malloc(size_bytes);

    if (memory == NULL) {
	perror("malloc failed: Not enough RAM");
	return 1;
    }

    // Touch the memory to make sure it actually gets allocated
    // 4096 is the size of a page so try to touch every page
    for (size_t i = 0; i < size_bytes; i += 4096) {
	memory[i] = 'A';
    }

    printf("Allocated %zu MB of memory. Press Ctrl+C to exit and return it.\n", size_mb);

    // Keep program running and holding the memory
    while (1) {
	sleep(1);
    }
    
    // Unreachable, but makes CS professors happy.
    // The OS will reclaim the memory on exit.
    free(memory);
    return 0;
}
