/*
	Name: C�lculos Num�ricos
	Author: Guilherme Bezerra
	Date: 08/04/23 00:51
	Description: Faz opera��es b�sicas de n�meros digitados pelo usu�rio
*/

//Se��o de Importa��o de Bibliotecas
#include <stdio.h>
#include <locale.h>

main()
{
	setlocale(LC_ALL, "Portuguese");
	float n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, n20, n21, n22, n23, n24, n25,T;
	n1=n2=n3=n4=n5=n6=n7=n8=n9=n10=n11=n12=n13=n14=n15=n16=n17=n18=n19=n20=n21=n22=n23=n24=n25 = 0.0;
	char sinal;
	sinal = ' ';
	
	printf("Apenas Adi��o (+), Subtra��o (-), Multiplica��o (*) e Divis�o (/). \n");
	puts("Limite de Opera��es Consecutivas: 25 \n");
	
	scanf("%f", &n1); //Memoriza o primeiro
	printf("O n�mero 1 �: %f \n", n1);
	
	scanf(" %c", &sinal); //Pega o sinal                         N�O EST� ACEITANDO VALOR DE "CHAR",
	printf("A opera��o �: %c \n", sinal);                              //SOMENTE NO COME�O
	
	scanf("%f", &n2); //Memoriza o segundo
	printf("O n�mero 2 �: %f \n", n2);
	
	if (sinal == '+'){
		T = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14+n15+n16+n17+n18+n19+n20+n21+n22+n23+n24+n25;
		printf("%f \n", T);}
	else if (sinal =='-'){
		T = n1-n2-n3-n4-n5-n6-n7-n8-n9-n10-n11-n12-n13-n14-n15-n16-n17-n18-n19-n20-n21-n22-n23-n24-n25,
		printf("%f \n", T);}
	else if (sinal == '*'){ //multiplica��o e divis�o n�o est�o funcionando pq sempre zera tudo
		T = n1*n2*n3*n4*n5*n6*n7*n8*n9*n10*n11*n12*n13*n14*n15*n16*n17*n18*n19*n20*n21*n22*n23*n24*n25,
		printf("%f \n", T);}
	else if (sinal == '/'){
		T = n1/n2/n3/n4/n5/n6/n7/n8/n9/n10/n11/n12/n13/n14/n15/n16/n17/n18/n19/n20/n21/n22/n23/n24/n25,
		printf("%f \n", T);}
	else printf("Apenas Adi��o (+), Subtra��o (-), Multiplica��o (*) e Divis�o (/). \n");
		
		
		
	//Como fazer uma calculadora usando C - n1n2n3n4n5n6n7n8n9n10n11n12n13n14n15n16n17n18n19n20n21n22n23n24n25
	//pq o usu�rio pode n�o digitar apenas 2 ou 3 n�meros (vari�veis INFINITAS?)
	//Resposta Poss�vel: Utilizar um n�mero m�ximo de vari�veis para n�meros... EX:25 vari�veis chamadas n1, n2, n3... n25.
}
