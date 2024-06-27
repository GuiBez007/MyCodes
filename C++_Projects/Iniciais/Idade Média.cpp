/*
	Name: Idade M�dia
	Author: GUilherme Bezerra
	Date: 25/04/2023 16:20
	Description: Calcula a idade m�dia entre 10 pessoas, separando o resultado entre masculino e feminino 
*/

//Importa��o de Bibliotecas
#include <stdio.h>
#include <locale.h>

main (){
	setlocale (LC_ALL, "Portuguese");
	float mediaM, mediaF;
	int idade, i, m, f; //a m�dia � dividida pelas vari�veis 'm' e 'f', que s�o contadores 
	char sexo;
	mediaM = mediaF = 0.0; idade = i = m = f = 0; sexo = ' ';
	
	while (i < 10){
		printf ("\nInforme seu g�nero (M/F): ");
		scanf (" %c", &sexo);
		printf ("Digite sua idade: ");
		scanf ("%d", &idade);
		
		if (sexo == 'M' || sexo == 'm'){
			mediaM = mediaM + idade;
			m++;}
		else if (sexo == 'F' || sexo == 'f'){
			mediaF = mediaF + idade;
			f++;}
		else{ printf ("Dado inv�lido!! \nTente novamente..\n");
			i--;} //serve para anular a contagem quando um dado inv�lido � informado (+1 com -1 d� 0)
	i++;}
	
	mediaM = mediaM /m;
	mediaF = mediaF /f;
	printf ("\nA m�dia masculina foi de %.2f e a m�dia feminina foi de %.2f.", mediaM, mediaF);
}
// ERRADO!!!! \/ \/
//	printf ("A m�dia masculina foi de %.2f", mediaM, " e a m�dia feminina foi de %.2f", mediaF);
// ERRADO!!!! /\ /\

