/*
  Name: Dumbinho's Candy
  Author: GUilherme Bezerra
  Date: 28/02/24 21:22
  Description: define if informed number is odd or pair and print dumbinho or 8-bonito
*/

// prototipation
void odd_pair(int);
int sum();

// libraries
#include <stdio.h>
#include <stdlib.h>

int main()
{
	// invoke the function in another function
	odd_pair(sum());
	return 0;
}

void odd_pair(int sum)
{
	// check if the number is odd or pair
	if (sum % 2 == 0)
		printf("dumbinho");
	else printf("8-bonito");
}

int sum()
{
	// gets a number in char_mode and converts him in an int number
    char candy_number[8];
    gets(candy_number);
    int aux = atoi(candy_number);
    
    // limiter between 1 and 1 milion
    if (aux < 1 || aux > 1000000)
    	exit(1); ///
    int code_sum = 0;
    
    // runs until the char ENTER -> '\0'
    for (int i=0; i != '\0'; i++)
    {
    	//code_sum += candy_number[i] - '0';
    	code_sum = code_sum + candy_number[i] - '0'; // ERROR!!!!!!!!!!!!!!!!!!!!!!
	}
	return code_sum;
}
