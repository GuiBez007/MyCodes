/*
	Name: !Primos Up!
	Author: GUilherme Bezerra
	Date: 28/08/23 10:01h
	Description: Numeros primos de uma outra forma
*/

//Libraries
#include <stdio.h>
#include <locale.h>

int main(){
	setlocale(LC_ALL, "Portuguese");
	int numero, count, resultado, vetor[5];
	
	//� para fazer o usu�rio digitar v�rios n�meros de uma vez
	puts("Digite os 5 n�meros a serem analisados: ");
	for (int i=0; i<5; i++){
		scanf("%d", &vetor[i]);
	}
	puts("");
	
	//Pega o n�mero no vetor
	for (int i=0; i<5; i++){
		count = 0;
		for (int x=1; x<=vetor[i]; x++){
			if (vetor[i] % x == 0)
				count++;
		}
		if (count == 2)
			printf("O n�mero %d � primo!\n", vetor[i]);
		else
			printf("O n�mero %d n�o � primo!\n", vetor[i]);
	}
getchar();
return 0;
	
}
