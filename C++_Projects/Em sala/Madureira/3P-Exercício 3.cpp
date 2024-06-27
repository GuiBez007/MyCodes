/*
	Name: 8 Números
	Author: GUilherme Bezerra
	Date: 04/09/23 20:39
	Description: Armazena 8 números em ordem crescente e mostra na tela
*/

//Libraries
#include <stdio.h>
#include <locale.h>

int main(){
	setlocale(LC_ALL, "Portuguese");
	int vetor_crescente[8], temp_1, temp_2;
	temp_1 = temp_2 = 0;
	
	//Inicializa o vetor(com valor 0)
	for (int i=0; i<8; i++)
		vetor_crescente[i] = 0;
	
	//Entrada dos valores inteiros	
	puts("Digite abaixo os 8 números:");
	for (int i=0; i<8; i++){
		scanf("%d", &temp_1);
		
		//Transfere sempre o maior valor a uma variável, e o armazena na última posição do vetor
		//de acordo com a quantidade de números já informados pelo usuário
		for (int x=0; x<=i; x++){
			if (temp_1 <= vetor_crescente[x]){
				temp_2 = vetor_crescente[x];
				vetor_crescente[x] = temp_1;
				temp_1 = temp_2;
			} 
			if (x==i)
				vetor_crescente[x] = temp_1;
		} 
	}
	//Saída final
	puts("");
	for (int i=0; i<8; i++)
		printf("%i ", vetor_crescente[i]);
	
getchar();
return 0;	
	
}
