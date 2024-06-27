/*
	Name: Tutorial
	Author: GUilherme Bezerra
	Date: 26/04/2023 19:12
	Description: Exibe um tutorial detalhado de acordo com a escolha do usu�rio.
*/

//Importa��o de Bibliotecas
#include <stdio.h>
#include <locale.h>
#include <Windows.h>

main (){
	setlocale (LC_ALL, "Portuguese");
	char numero;
	int i_principal, n1, n2, n3, i, x, exemplo;
	n1 = n2 = n3 = i = x = 0; numero = ' ';
	
	for (i_principal = 0; i_principal >= 0; i_principal++){
	i = 0;
	while (i == 0){ 
		puts ("===========================================");
		puts ("'TUTORIAL || HIST�RICO' DE APRENDIZADO ");
		puts ("===========================================");
		puts ("Para navegar entre t�picos, digite o n�mero correspondente:");
		puts ("[01] - para regras b�sicas e pequenos macetes da linguagem C;");
		puts ("#[02] - (s� esse est� pronto) para saber sobre os comandos [printf, scanf, puts...];");
		puts ("[03] - para condicionais [if, else, else if];");
		puts ("[04] - para la�os de repeti��o [while, do..while, for];");
		puts ("[05] - ...");
		n1 = n2 = n3 = x = 0;
		printf ("N�mero: ");
		scanf ("%d", &n1); 
		system ("cls");
		
		while (x == 0){
			//para n�mero n�o tem diferen�a entre 1/01/001...  
			if (n1 == 02){                                                        //op��o geral-02
				puts ("Deseja uma explica��o mais detalhada ou espec�fica?");
				puts ("[00] - voltar;");
				puts ("[01] - mais detalhada.");
				puts ("[02] - mais expec�fica;");
				n2 = 0;
				printf ("N�mero: "); 
				scanf ("%d", &n2);
				system ("cls");
				
				if (n2 == 0 || n2 == 00){
					system ("cls");
					x++;
				}
				else if (n2 == 1 || n2 == 01){
					while (x == 0){
						switch (n2){
						case 0:
							x++;
							system ("cls");
						break;
						
						case 1:
							puts ("PRINTF");
							puts ("===========================");
							puts ("O 'printf(\"\")' mostra na tela tudo o que for digitado dentro das aspas duplas (\"\").");
							puts ("Por meio dele podemos nos comunicar, de certa forma, com quem estiver utilizando o programa.");
							puts ("EXEMPLO: printf(\"Oi Felipe, tudo bem?\");");
							puts ("RESULTADO: Oi Felipe, tudo bem?");
							puts ("\nO resultado � o que ser� mostrado na tela de output; o texto entre aspas � denominado uma string.");
							puts ("Podemos tamb�m utilizar esse comando para chamar uma vari�vel dentro da string.");
							puts ("EXEMPLO: printf(\"A profundidade da piscina � de %d metros.\", altura_piscina);");
							puts ("RESULTADO[30]: A profundidade da piscina � de 30 metros.");
							puts ("\n\n\n\n[00] - In�cio                                                                         [02]-ir para PUTS->");
							scanf ("%d", &n2);
							system ("cls");
						break;
						
						case 2:	
							puts ("PUTS");
							puts ("===========================");
							puts ("O 'puts(\"\")' faz o mesmo que o printf, s� que aceita apenas strings em seu corpo (n�o vari�veis).");
							puts ("EXEMPLO V�LIDO: puts(\"Estou, j� comi 3 vezes hoje.\");");
							puts ("EXEMPLO INV�LIDO: puts(\"Estou, j� comi %d vezes hoje\", variavel_vezes);");
							puts ("\nOutra coisa que muda entre esses dois comandos � que o 'puts()' pula para a pr�xima linha ap�s sua execu��o.");
							puts ("J� o 'printf()' n�o. Caso digitasse 2 comandos 'printf()' um embaixo do outro, no output seria mostrada uma string \nap�s a outra, em uma mesma linha.");
							puts ("\nputs(\"A porta \");");
							puts ("puts(\"est� fechada.\");");
							puts ("RESULTADO: A porta");
							puts ("           est� fechada.");
							puts ("\nOBS: no 'printf()' ficaria: A porta est� fechada. - TUDO NA MESMA LINHA");
							puts ("\n\n\n\n[00] - In�cio                                           <-voltar para PRINTF-[01] || [02]-ir para SCANF->");
							scanf ("%d", &n2);
							if (n2 == 2)
								n2 = n2 +1;
							system ("cls");
						break;
						
						case 3:
							puts ("SCANF");
							puts ("===========================");
							puts ("O 'scanf(\"\")' � utilizado para pegar informa��es que um usu�rio digite e as guardar em uma vari�vel j� existente.");
							printf ("POR EXEMPLO: Quantas vezes voc� comeu hoje?_DIGITE UM N�MERO: ");
							scanf ("%d", &exemplo); Sleep (500); printf ("."); Sleep (500); printf ("."); Sleep (500); printf ("."); Sleep (500);
							if (exemplo == 1)
								printf ("Voc� s� comeu %d vez mesmo?", exemplo), Sleep (1200);
							else if (exemplo > 1) 
								printf ("Voc� comeu %d vezes mesmo?", exemplo), Sleep (1400);
							else printf ("Uma carninha de vez em quando faz bem, viu?!");
							
							puts ("\n\nO que fiz foi estruturar o 'scanf()' desta forma: scanf(\"%d\", &n�merodevezes);");
							puts ("Onde: \"%d\" � o tipo de vari�vel a ser lida ('d' � de decimal) e ap�s a v�rgula, o nome da vari�vel a receber \no valor informado.");
							if (exemplo <= 0){
								printf (" ____________________________________________________________________________   _____");
								printf ("\n/TERIA DADO CERTO SE O USU�RIO N�O TIVESSE 'ESTRAGADO' TUDO...SEU DESNUTRIDO!\\ |`@ @�|");
								printf ("\n\\____________________________________________________________________________/ |__~__|");
								printf ("\nUma preocupa��o que devemos sempre ter em mente.                                <|-|>");
							}
							else printf ("OBS: o '&' � necess�rio antes do nome da vari�vel a ser lida, portanto, utiliza-se '&' apenas em scanf (em printf n�o).");
							if (exemplo == 1)
								puts ("\n\nPara mostrar o resultado ao usu�rio, usei: printf (\"Voc� s� comeu %d vez mesmo?\", numerodevezes);");
							else puts ("\n\nPara mostrar o resultado ao usu�rio, usei: printf (\"Voc� comeu %d vezes mesmo?\", numerodevezes);");
							
							puts ("Onde: %d representa o local que a vari�vel vai assumir na string e, depois da v�rgula qual o nome da vari�vel que ir� \nassumir a posi��o %d.");
							puts ("\n\n\n\n[00] - In�cio                                            <-voltar para PUTS-[01]");
							scanf ("%d", &n2);
							if (n2 == 1)
								n2 = n2 + 1;
							system ("cls");
						break;
						}
					}
				}
				else if (n2 == 2 || n2 == 02){
					while (i == 0){
						puts ("[00] - voltar;");
						puts ("[01] - sobre printf();");
						puts ("[02] - sobre puts();");
						puts ("[03] - sobre scanf().");
						printf ("N�mero: ");
						scanf ("%d", &n3);
						system ("cls");
						
						if (n3 == 0 || n3 == 00){
							i = 1;
							x++; 
						}
						else{
						switch (n3){ //OBS: o case serve para 1/01/001/0001/00001.....
							case 1:
								puts ("======================================================");
								puts ("FUNCIONAMENTO DO PRINTF");
								puts ("======================================================");
								puts ("printf(\"Maria foi \");");
								puts ("printf(\"� feira:\\n%d vezes.\", numero_vezes);");
								puts ("\nRESULTADO[30]: Maria foi � feira:");
								puts ("               30 vezes.");
								puts ("======================================================");
							break;
							
							case 2:
								puts ("======================================================");
								puts ("FUNCIONAMENTO DO PUTS");
								puts ("======================================================");
								puts ("EX1: puts(\"O professor escreveu um S\")");
								puts ("     puts(\"na lousa.\");");
								puts ("EX2: \n     puts(\"O professor escreveu um %c\")");
								puts ("     puts(\"na lousa.\", letra_na_lousa);");
								puts ("\nRESULTADO: EX1: O professor escreveu um S");
								puts ("                na lousa.");
								puts ("           EX2: Error ('puts' apenas para strings).");
								puts ("======================================================");
							break;
						
							case 3:
								puts ("======================================================");
								puts ("FUNCIONAMENTO DO SCANF");
								puts ("======================================================");
								puts ("Quantos anos voc� tem?_");
								puts ("scanf(\"%d\", &idade);");
								puts ("printf(\"O usu�rio tem %d anos.\", idade);");
								puts ("\nRESULTADO[30]: O usu�rio tem 30 anos.");
								puts ("======================================================");
							break;
						}}
					}
				}
			}
			else{
				puts("Em desenvolvimento!");
				system("pause");
				system("cls");
				break;
			}
		}	
	}}
}
