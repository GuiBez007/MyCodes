/*
	Name: M�dia 40
	Author : GUilherme Bezerra
	Date: 25/04/2023 18:03
	Description: Calcula a m�dia (4 notas) de 40 alunos
*/

//Importa��o de Bibliotecas
#include <stdio.h>
#include <locale.h>

main (){
	setlocale (LC_ALL, "Portuguese");
	float nota, media;
	int i, x;
	nota = media = 0.0; i = 1;
	
	while (i <= 40){ //contador geral (para os alunos)
		for (x = 0; x < 4; x++){ //contador para as respectivas notas
			printf ("Nota: ");
			scanf ("%f", &nota); //pega as notas
			media = media + nota;} //armazena em m�dia
		media = media /x; //divide a soma das notas (armazenadas em m�dia) por x (que vale 4)
		printf ("A m�dia do %d� aluno �: %.2f\n\n", i, media);
		media = 0.0; i++;} //zera a media e sobe contador
			
} 
//COMO CALCULAR A M�DIA DOS 40 ALUNOS E MOSTRAR TODAS APENAS NO FINAL?
