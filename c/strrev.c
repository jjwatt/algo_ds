/* In place string reversal in C */

#include <stdio.h>

int string_length(char*);
void reverse_in_place(char*);

int main(int argc, char **argv)
{
	char* s;

	if (argc > 1) {
		s = argv[1];
		printf("Reverse of the string \"%s\".\n", s);
		printf("Reversing...");
		reverse_in_place(s);
		printf("Reversal: \"%s\"\n", s);
		return 0;
	} else {
		printf("Please provide a string to reverse.\n");
		return 1;
	}
}

void reverse_in_place(char *strin)
{
	int length, c;
	char *begin, *end, temp;

	length = string_length(strin);
	/* Point both pointers at the string */
	begin = strin;
	end = strin;

	/* Fast forward end pointer to the end */
	/* e.g., '[0] c, [1] a, [2] t */
	/* end -> strin[2] */
	for (c = 0; c < length - 1; c++)
		end++;

	for (c = 0; c < length/2; c++)
	{
		temp = *end;
		*end = *begin;
		*begin = temp;
		begin++;
		end--;
	}
}


int string_length(char *pointer)
{
	int counter = 0;
	while ( *(pointer + counter) != '\0' )
		counter++;
	return counter;
}
