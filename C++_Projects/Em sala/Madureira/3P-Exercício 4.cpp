/*
	Name: Vetores XYZ
	Author: GUilherme Bezerra
	Date: 10/09/23 11:36
	Description: Cálculos utilizando vetores
*/

//Libraries
#include <stdio.h>
#include <locale.h>
#include <math.h>

int main(){
	setlocale(LC_ALL, "Portuguese");
	int vetor_x[20];
	float vetor_y[20], vetor_z[20];

	//Armazena os valores digitados pelo usuário no vetor X, multiplica 
	//por 100 e joga no Y, divide os de Y por X e os coloca em Z
	puts("Digite abaixo os valores:");
	for (int x=0; x<20; x++){
		scanf("%i", &vetor_x[x]);
		vetor_y[x] = vetor_x[x] *100;
		vetor_z[x] = vetor_y[x] /vetor_x[x];
	}
	
	//Mostra cada valor de cada vetor
	for (int i=0; i<3; i++){
		if (i==0){
			printf("\nVetor X = ");
			for (int count=0; count<20; count++)
				printf("%i    ", vetor_x[count]);
		}
		else if (i==1){
			printf("\nVetor Y = ");
			for (int count=0; count<20; count++)
				printf("%.0f  ", vetor_y[count]);
		}
		else if (i==2){
			printf("\nVetor Z = ");
			for (int count=0; count<20; count++)
				printf("%.0f  ", vetor_z[count]);
		}
	}
	
getchar();
return 0;
	
}

