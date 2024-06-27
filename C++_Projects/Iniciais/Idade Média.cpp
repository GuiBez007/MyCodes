/*
	Name: Idade Média
	Author: GUilherme Bezerra
	Date: 25/04/2023 16:20
	Description: Calcula a idade média entre 10 pessoas, separando o resultado entre masculino e feminino 
*/

//Importação de Bibliotecas
#include <stdio.h>
#include <locale.h>

main (){
	setlocale (LC_ALL, "Portuguese");
	float mediaM, mediaF;
	int idade, i, m, f; //a média é dividida pelas variáveis 'm' e 'f', que são contadores 
	char sexo;
	mediaM = mediaF = 0.0; idade = i = m = f = 0; sexo = ' ';
	
	while (i < 10){
		printf ("\nInforme seu gênero (M/F): ");
		scanf (" %c", &sexo);
		printf ("Digite sua idade: ");
		scanf ("%d", &idade);
		
		if (sexo == 'M' || sexo == 'm'){
			mediaM = mediaM + idade;
			m++;}
		else if (sexo == 'F' || sexo == 'f'){
			mediaF = mediaF + idade;
			f++;}
		else{ printf ("Dado inválido!! \nTente novamente..\n");
			i--;} //serve para anular a contagem quando um dado inválido é informado (+1 com -1 dá 0)
	i++;}
	
	mediaM = mediaM /m;
	mediaF = mediaF /f;
	printf ("\nA média masculina foi de %.2f e a média feminina foi de %.2f.", mediaM, mediaF);
}
// ERRADO!!!! \/ \/
//	printf ("A média masculina foi de %.2f", mediaM, " e a média feminina foi de %.2f", mediaF);
// ERRADO!!!! /\ /\

