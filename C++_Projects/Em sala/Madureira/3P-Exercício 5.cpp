/*
	Name: Vetor Vetor V-Invertido
	Author: GUilherme Bezerra 
	Date: 10/09/23 12:10
	Description: Armazena números divisíveis por 3 e 10 e joga a subtração em outro vetor
*/

//Libraries
#include <stdio.h>
#include <locale.h>

int main(){
	setlocale(LC_ALL, "Portuguese");
	int teste, vetor_k[10], vetor_l[10], vetor_m[10];
	
	//Entrada dos 20 números
	puts("Digite abaixo 10 números divisíveis por 3:");
	for (int i=0; i<10; i++){ 
		scanf("%i", &teste);
		if (teste %3 == 0)
			vetor_k[i] = teste;
		else i--;
	}
	puts("\nAgora 10 números divisíveis por 10:");
	for (int i=0; i<10; i++){ 
		scanf("%i", &teste);
		if (teste %10 == 0)
			vetor_l[i] = teste;
		else i--;
	}
	
	//Saída de todos os valores(Vetor-L em ordem de input)
	puts("\nVetor-K     Vetor-L     Vetor-M");
	int decrementador = 10; 
	for (int i=0; i<10; i++){ 
		decrementador --;
		vetor_m[i] = vetor_k[i] - vetor_l[decrementador];
		printf("   %i          %i          %i\n", vetor_k[i], vetor_l[i], vetor_m[i]);
	}
	
getchar();
return 0;
	
}
