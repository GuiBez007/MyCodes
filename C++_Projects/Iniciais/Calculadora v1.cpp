/*
	Name: Cálculos Numéricos
	Author: Guilherme Bezerra
	Date: 08/04/23 00:51
	Description: Faz operações básicas de números digitados pelo usuário
*/

//Seção de Importação de Bibliotecas
#include <stdio.h>
#include <locale.h>

main()
{
	setlocale(LC_ALL, "Portuguese");
	float n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, n20, n21, n22, n23, n24, n25,T;
	n1=n2=n3=n4=n5=n6=n7=n8=n9=n10=n11=n12=n13=n14=n15=n16=n17=n18=n19=n20=n21=n22=n23=n24=n25 = 0.0;
	char sinal;
	sinal = ' ';
	
	printf("Apenas Adição (+), Subtração (-), Multiplicação (*) e Divisão (/). \n");
	puts("Limite de Operações Consecutivas: 25 \n");
	
	scanf("%f", &n1); //Memoriza o primeiro
	printf("O número 1 é: %f \n", n1);
	
	scanf(" %c", &sinal); //Pega o sinal                         NÃO ESTÁ ACEITANDO VALOR DE "CHAR",
	printf("A operação é: %c \n", sinal);                              //SOMENTE NO COMEÇO
	
	scanf("%f", &n2); //Memoriza o segundo
	printf("O número 2 é: %f \n", n2);
	
	if (sinal == '+'){
		T = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14+n15+n16+n17+n18+n19+n20+n21+n22+n23+n24+n25;
		printf("%f \n", T);}
	else if (sinal =='-'){
		T = n1-n2-n3-n4-n5-n6-n7-n8-n9-n10-n11-n12-n13-n14-n15-n16-n17-n18-n19-n20-n21-n22-n23-n24-n25,
		printf("%f \n", T);}
	else if (sinal == '*'){ //multiplicação e divisão não estão funcionando pq sempre zera tudo
		T = n1*n2*n3*n4*n5*n6*n7*n8*n9*n10*n11*n12*n13*n14*n15*n16*n17*n18*n19*n20*n21*n22*n23*n24*n25,
		printf("%f \n", T);}
	else if (sinal == '/'){
		T = n1/n2/n3/n4/n5/n6/n7/n8/n9/n10/n11/n12/n13/n14/n15/n16/n17/n18/n19/n20/n21/n22/n23/n24/n25,
		printf("%f \n", T);}
	else printf("Apenas Adição (+), Subtração (-), Multiplicação (*) e Divisão (/). \n");
		
		
		
	//Como fazer uma calculadora usando C - n1n2n3n4n5n6n7n8n9n10n11n12n13n14n15n16n17n18n19n20n21n22n23n24n25
	//pq o usuário pode não digitar apenas 2 ou 3 números (variáveis INFINITAS?)
	//Resposta Possível: Utilizar um número máximo de variáveis para números... EX:25 variáveis chamadas n1, n2, n3... n25.
}
