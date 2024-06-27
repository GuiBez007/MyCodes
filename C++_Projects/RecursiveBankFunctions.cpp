/*
	Name: RecursividadeBancaria.cpp
	Author: GUilherme Bezerra
	Date: 21/03/24 19:05
	Description: Training the recursive functions in a bank example
*/

// Libraries
#include <stdio.h>
#include <stdlib.h>

// Prototipation
void Deposit();
void Withdraw();
void SeeBalance();
void Login();
void Password();
void ChangePassword();

// Global functions
float _balance = 0.0;
char _current_user = 'G';
int _current_password = 0;



// The main function
int main()
{
	int operation = 0;
	puts("What operation do you wish to do?");
	puts("========================================");
	puts("[1] - See current balance;");
	puts("[2] - Deposit a value;");
	puts("[3] - Withdraw a value;");
	puts("[4] - Change account password;");
	printf("\nI want to do the operation number: ");
	scanf(" %i", &operation);
	system("cls");
	
	switch (operation)
	{
		case 1:
			SeeBalance();
			break;
		case 2:
			Deposit();
			break;
		case 3:
			Withdraw();
			break;
		case 4:
			ChangePassword();
			break;
	}
	
	return 0;
}



// To see the user current balance
void SeeBalance()
{
	printf("Your actual balance is: $%.2f \n", _balance);
	printf("\nAnything else? \n");
	main();
}



// To deposit money in the user account
void Deposit()
{
	float deposit_value = 0.0;
	printf("Type the value that will be transfered: ");
	scanf(" %f", &deposit_value);
	_balance += deposit_value;
	
	printf("\nAnything else? \n");
	main();
}



// To withdraw money of the user account
void Withdraw()
{
	float withdraw_value = 0.0;
	
	Login();
	
	printf("Type the value that will be withdrawn: ");
	scanf(" %f", &withdraw_value);
	_balance -= withdraw_value;
	
	printf("\nAnything else? \n");
	main();
}



// To change the user account password
void ChangePassword()
{
	printf("Actual ");
	Password();
	//
}



// User login verification
void Login()
{
	char user = ' ';
	printf("User: ");
	scanf(" %c", &user);
	
	if (user == _current_user)
		Password();
	else
	{
		puts("Incorrect user. Try again!");
		Login();
	}
}



// User password verification
void Password()
{
	int password = 0;
	printf("Password: ");
	scanf(" %c", &password);
	
	if (password == _current_password)
		printf("Login with sucess!");
	else
	{
		puts("Incorrect information. Try again!");
		Password();
	}
}
