/*
	Name: Tutorial
	Author: GUilherme Bezerra
	Date: 26/04/2023 19:12
	Description: Exibe um tutorial detalhado de acordo com a escolha do usuário.
*/

//Importação de Bibliotecas
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
		puts ("'TUTORIAL || HISTÓRICO' DE APRENDIZADO ");
		puts ("===========================================");
		puts ("Para navegar entre tópicos, digite o número correspondente:");
		puts ("[01] - para regras básicas e pequenos macetes da linguagem C;");
		puts ("#[02] - (só esse está pronto) para saber sobre os comandos [printf, scanf, puts...];");
		puts ("[03] - para condicionais [if, else, else if];");
		puts ("[04] - para laços de repetição [while, do..while, for];");
		puts ("[05] - ...");
		n1 = n2 = n3 = x = 0;
		printf ("Número: ");
		scanf ("%d", &n1); 
		system ("cls");
		
		while (x == 0){
			//para número não tem diferença entre 1/01/001...  
			if (n1 == 02){                                                        //opção geral-02
				puts ("Deseja uma explicação mais detalhada ou específica?");
				puts ("[00] - voltar;");
				puts ("[01] - mais detalhada.");
				puts ("[02] - mais expecífica;");
				n2 = 0;
				printf ("Número: "); 
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
							puts ("\nO resultado é o que será mostrado na tela de output; o texto entre aspas é denominado uma string.");
							puts ("Podemos também utilizar esse comando para chamar uma variável dentro da string.");
							puts ("EXEMPLO: printf(\"A profundidade da piscina é de %d metros.\", altura_piscina);");
							puts ("RESULTADO[30]: A profundidade da piscina é de 30 metros.");
							puts ("\n\n\n\n[00] - Início                                                                         [02]-ir para PUTS->");
							scanf ("%d", &n2);
							system ("cls");
						break;
						
						case 2:	
							puts ("PUTS");
							puts ("===========================");
							puts ("O 'puts(\"\")' faz o mesmo que o printf, só que aceita apenas strings em seu corpo (não variáveis).");
							puts ("EXEMPLO VÁLIDO: puts(\"Estou, já comi 3 vezes hoje.\");");
							puts ("EXEMPLO INVÁLIDO: puts(\"Estou, já comi %d vezes hoje\", variavel_vezes);");
							puts ("\nOutra coisa que muda entre esses dois comandos é que o 'puts()' pula para a próxima linha após sua execução.");
							puts ("Já o 'printf()' não. Caso digitasse 2 comandos 'printf()' um embaixo do outro, no output seria mostrada uma string \napós a outra, em uma mesma linha.");
							puts ("\nputs(\"A porta \");");
							puts ("puts(\"está fechada.\");");
							puts ("RESULTADO: A porta");
							puts ("           está fechada.");
							puts ("\nOBS: no 'printf()' ficaria: A porta está fechada. - TUDO NA MESMA LINHA");
							puts ("\n\n\n\n[00] - Início                                           <-voltar para PRINTF-[01] || [02]-ir para SCANF->");
							scanf ("%d", &n2);
							if (n2 == 2)
								n2 = n2 +1;
							system ("cls");
						break;
						
						case 3:
							puts ("SCANF");
							puts ("===========================");
							puts ("O 'scanf(\"\")' é utilizado para pegar informações que um usuário digite e as guardar em uma variável já existente.");
							printf ("POR EXEMPLO: Quantas vezes você comeu hoje?_DIGITE UM NÚMERO: ");
							scanf ("%d", &exemplo); Sleep (500); printf ("."); Sleep (500); printf ("."); Sleep (500); printf ("."); Sleep (500);
							if (exemplo == 1)
								printf ("Você só comeu %d vez mesmo?", exemplo), Sleep (1200);
							else if (exemplo > 1) 
								printf ("Você comeu %d vezes mesmo?", exemplo), Sleep (1400);
							else printf ("Uma carninha de vez em quando faz bem, viu?!");
							
							puts ("\n\nO que fiz foi estruturar o 'scanf()' desta forma: scanf(\"%d\", &númerodevezes);");
							puts ("Onde: \"%d\" é o tipo de variável a ser lida ('d' é de decimal) e após a vírgula, o nome da variável a receber \no valor informado.");
							if (exemplo <= 0){
								printf (" ____________________________________________________________________________   _____");
								printf ("\n/TERIA DADO CERTO SE O USUÁRIO NÃO TIVESSE 'ESTRAGADO' TUDO...SEU DESNUTRIDO!\\ |`@ @´|");
								printf ("\n\\____________________________________________________________________________/ |__~__|");
								printf ("\nUma preocupação que devemos sempre ter em mente.                                <|-|>");
							}
							else printf ("OBS: o '&' é necessário antes do nome da variável a ser lida, portanto, utiliza-se '&' apenas em scanf (em printf não).");
							if (exemplo == 1)
								puts ("\n\nPara mostrar o resultado ao usuário, usei: printf (\"Você só comeu %d vez mesmo?\", numerodevezes);");
							else puts ("\n\nPara mostrar o resultado ao usuário, usei: printf (\"Você comeu %d vezes mesmo?\", numerodevezes);");
							
							puts ("Onde: %d representa o local que a variável vai assumir na string e, depois da vìrgula qual o nome da variável que irá \nassumir a posição %d.");
							puts ("\n\n\n\n[00] - Início                                            <-voltar para PUTS-[01]");
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
						printf ("Número: ");
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
								puts ("printf(\"à feira:\\n%d vezes.\", numero_vezes);");
								puts ("\nRESULTADO[30]: Maria foi à feira:");
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
								puts ("Quantos anos você tem?_");
								puts ("scanf(\"%d\", &idade);");
								puts ("printf(\"O usuário tem %d anos.\", idade);");
								puts ("\nRESULTADO[30]: O usuário tem 30 anos.");
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
