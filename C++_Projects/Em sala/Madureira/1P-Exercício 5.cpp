/*
	Name: Tipos Sanguíneos
	Author: GUilherme Bezerra
	Date: 04/09/23 16:00
	Description: Analisa as informações e mostra o tipo de saengue compatível com o informado
*/   

//Libraries
#include <stdio.h>
#include <locale.h>
#include <conio.h>

int main(){
	setlocale(LC_ALL, "Portuguese");
	int codigo;
	
	//Instrução visual
	printf("CÓDIGO      TIPO SANGUÍNEO\
			\n  1...............O-	  \
			\n  2...............O+	  \
			\n  3...............A- 	  \
			\n  4...............A+	  \
			\n  5...............B-	  \
			\n  6...............B+	  \
			\n  7...............AB-	  \
			\n  8...............AB+	  \n");
	printf("\nInforme seu tipo sanguíneo: ");
	scanf("%i", &codigo);
	
	//Condições e saída final
	switch (codigo){
		case 1:
			printf("Pode receber O-");
			break;
		case 2:
			printf("Pode receber O- e O+");
			break;
		case 3:
			printf("Pode receber O- e A-");
			break;
		case 4:
			printf("Pode receber O-, O+, A- e A+");
			break;
		case 5:
			printf("Pode receber O- e B-");
			break;
		case 6:
			printf("Pode receber O-, O+, B- e B+");
			break;
		case 7:
			printf("Pode receber O-, A-, B- e AB-");
			break;
		case 8:
			printf("Pode receber O-, O+, A-, A+, B-, B+, AB- e AB+");
			break;
	}
	
getch();
return 0;
	
}
//conio.h e getch() para não fechar sozinho
//gets() para pegar string inteira com espaço
//%s não precisa expor tamanho do array de char 
