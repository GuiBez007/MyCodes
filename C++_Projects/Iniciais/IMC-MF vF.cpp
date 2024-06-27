/*
	Name: IMC
	Author: Guilherme Bezerra
	Date: 04/04/2023 19:30
	Description: Calcula e classifica IMC de acordo com o sexo.
*/

//Seção de importação de bibliotecas
#include <stdio.h>
#include <locale.h>

main()
{
	setlocale(LC_ALL, "Portuguese");
	float peso, altura, IMC;
	char sexo;
	peso = altura = IMC = 0.0; sexo = ' ';
	
	puts("VEJA QUAL É O SEU IMC!");
	puts("================================");
	puts("Informe seu gênero (M/F): ");
	scanf("%c", &sexo);	//Digitar o Sexo
	if (sexo != 'M' && sexo != 'm' && sexo != 'F' && sexo != 'f')
		puts("O dado digitado está incorreto!"),
		puts("Para tentar novamente pressione qualquer tecla");
	else if (peso == 0.0)
		puts("Informe seu peso (em KG): "), 
		scanf("%f", &peso);	//Digitar o peso
		
		{if (sexo != 'M'  && sexo != 'm' && sexo != 'F' && sexo != 'f')
			printf("");
		else if (peso <= 0 || peso == 'a' || peso == 'b' || peso == 'c' || peso == 'd' || peso == 'e' || peso == 'f' || peso == 'g' || peso == 'h' || peso == 'i' || peso == 'j' || peso == 'k' || peso == 'l' || peso == 'm' || peso == 'n' || peso == 'o' || peso == 'p' || peso == 'q' || peso == 'r' || peso == 's' || peso == 't' || peso == 'u' || peso == 'v' || peso == 'w' || peso == 'x' || peso == 'y' || peso == 'z' || peso == 'ç' || peso == '"' || peso == '@' || peso== '#' || peso== '$' || peso == '%' || peso == '¨' || peso == '&' || peso == '!'|| peso == '*' || peso == '(' || peso == ')' || peso == '_' || peso == '-' || peso == '=' || peso == '§' || peso == '´' || peso == '`' || peso == '{' || peso == '}' || peso == '[' || peso == ']' || peso == 'ª' || peso == 'º' || peso == '^' || peso == '~' || peso == '/' || peso == '°' || peso == '|' || peso == '?' || peso == ':' || peso == ';' || peso == '.' || peso == ',' || peso == '<' || peso == '>' || peso == '+' || peso == 'B' || peso == 'C' || peso == 'D' || peso == 'E' || peso == 'F' || peso == 'G' || peso == 'H' || peso == 'I' || peso == 'J' || peso == 'K' || peso == 'L' || peso == 'M' || peso == 'N' || peso == 'O' || peso == 'P' || peso == 'Q' || peso == 'R' || peso == 'S' || peso == 'T' || peso == 'U' || peso == 'V' || peso == 'W' || peso == 'X' || peso == 'Y' || peso == 'Z' || peso == 'Ç')	
			puts("O peso informado está incorreto!"),
			puts("Para tentar novamente pressione qualquer tecla");
			else if (altura == 0.0)
				puts("Informe sua altura (separada por vírgula): "), 
				scanf("%f", &altura);}	//Digitar a altura
		{if (sexo != 'M' && sexo != 'm' && sexo != 'F' && sexo != 'f') 
			printf("");
		else if (peso <= 0 || peso == 'a' || peso == 'b' || peso == 'c' || peso == 'd' || peso == 'e' || peso == 'f' || peso == 'g' || peso == 'h' || peso == 'i' || peso == 'j' || peso == 'k' || peso == 'l' || peso == 'm' || peso == 'n' || peso == 'o' || peso == 'p' || peso == 'q' || peso == 'r' || peso == 's' || peso == 't' || peso == 'u' || peso == 'v' || peso == 'w' || peso == 'x' || peso == 'y' || peso == 'z' || peso == 'ç' || peso == '"' || peso == '@' || peso== '#' || peso== '$' || peso == '%' || peso == '¨' || peso == '&' || peso == '!'|| peso == '*' || peso == '(' || peso == ')' || peso == '_' || peso == '-' || peso == '=' || peso == '§' || peso == '´' || peso == '`' || peso == '{' || peso == '}' || peso == '[' || peso == ']' || peso == 'ª' || peso == 'º' || peso == '^' || peso == '~' || peso == '/' || peso == '°' || peso == '|' || peso == '?' || peso == ':' || peso == ';' || peso == '.' || peso == ',' || peso == '<' || peso == '>' || peso == '+' || peso == 'B' || peso == 'C' || peso == 'D' || peso == 'E' || peso == 'F' || peso == 'G' || peso == 'H' || peso == 'I' || peso == 'J' || peso == 'K' || peso == 'L' || peso == 'M' || peso == 'N' || peso == 'O' || peso == 'P' || peso == 'Q' || peso == 'R' || peso == 'S' || peso == 'T' || peso == 'U' || peso == 'V' || peso == 'W' || peso == 'X' || peso == 'Y' || peso == 'Z' || peso == 'Ç')
			printf("");
		else if (altura <= 0 || altura == 'a' || altura == 'b' || altura == 'c' || altura == 'd' || altura == 'e' || altura == 'f' || altura == 'g' || altura == 'h' || altura == 'i' || altura == 'j' || altura == 'k' || altura == 'l' || altura == 'm' || altura == 'n' || altura == 'o' || altura == 'p' || altura == 'q' || altura == 'r' || altura == 's' || altura == 't' || altura == 'u' || altura == 'v' || altura == 'w' || altura == 'x' || altura == 'y' || altura == 'z' || altura == 'ç' || altura == 'B' || altura == 'C' || altura == 'D' || altura == 'E' || altura == 'F' || altura == 'G' || altura == 'H' || altura == 'I' || altura == 'J' || altura == 'K' || altura == 'L' || altura == 'M' || altura == 'N' || altura == 'O' || altura == 'P' || altura == 'Q' || altura == 'R' || altura == 'S' || altura == 'T' || altura == 'U' || altura == 'V' || altura == 'W' || altura == 'X' || altura == 'Y' || altura == 'Z' || altura == 'Ç' || altura == '"' || altura == '@' || altura== '#' || altura== '$' || altura == '%' || altura == '¨' || altura == '&' || altura == '!'|| altura == '*' || altura == '(' || altura == ')' || altura == '_' || altura == '-' || altura == '=' || altura == '§' || altura == '´' || altura == '`' || altura == '{' || altura == '}' || altura == '[' || altura == ']' || altura == 'ª' || altura == 'º' || altura == '^' || altura == '~' || altura == '/' || altura == '°' || altura == '|' || altura == '?' || altura == ':' || altura == ';' || altura == '.' || altura == ',' || altura == '<' || altura == '>' || altura == '+')	
			puts("A altura informada está incorreta!"),
			puts("Para tentar novamente pressione qualquer tecla");
		else if (altura > 0);}
		
	IMC = peso/(altura*altura);
	if (sexo == 'M' || sexo == 'm'){
			if (peso <= 0)
				printf("");
			else if (IMC >= 0 && IMC < 20)
				puts("Algum dado foi digitado incorretamente!"),
				puts("Para tentar novamente, aperte qualquer tecla!");
				else if (IMC < 25)
					puts("Classificação: Normal");
					else if (IMC < 30)
						puts("Classificação: Levemente Obeso");
						else if (IMC < 35)
							puts("Classificação: Obesidade Grau I");
							else if (IMC < 40)
								puts("Classificação: Obesidade Grau II");
								else if (IMC <100)
									puts("Classificação: Obesidade Grau III");
									else puts("");}	
	if (sexo == 'F' || sexo == 'f'){
		if (peso <= 0)
			printf("");
		else if (IMC < 19)
			puts("Algum dado foi digitado incorretamente!"),
			puts("Para tentar novamente, aperte qualquer tecla!");
			else if (IMC < 24)
				puts("Classificação: Normal");
				else if (IMC < 29)
					puts("Classificação: Levemente Obeso");
					else if (IMC < 34)
						puts("Classificação: Obesidade Grau I");
						else if (IMC < 39)
							puts("Classificação: Obesidade Grau II");
							else if (IMC < 100) 
								puts("Classificação: Obesidade Grau III");
								else puts("");}	
}
