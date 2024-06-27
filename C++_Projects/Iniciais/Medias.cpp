/*
	Name: Aprovado e Reprovado
	Author: GUilherme Bezerra
	Date: 18/04/2023 21:52
	Description: calculo de média
*/

//Importação de Bibliotecas
#include <stdio.h>
#include <locale.h>

main(){
	setlocale (LC_ALL, "Portuguese");
	float nota1, nota2, media;
	int faltas, i;
	nota1 = nota2 = media = 0.0; faltas = i = 0;
	
	
	while (i == 0){
		printf ("Digite a primeira nota: ");
		scanf ("%f", &nota1);
		printf ("Digite a segunda nota: ");
		scanf ("%f", &nota2);
		printf ("Informe o total de faltas: ");
		scanf ("%d", &faltas);
		media = (nota1 + nota2) /2; //até aqui identifica a média e as faltas
		
		if (nota1 < 0 && nota2 < 0 && faltas < 0)
			i = -1;
		else if (media >= 6 && faltas < 10)
			printf ("Aprovado!\n\n");
		else printf ("Reprovado!\n\n");}
	
	
	
	
	
	
}
