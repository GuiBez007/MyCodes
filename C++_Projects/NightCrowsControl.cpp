/*
	Name: NightCrowsControl.cpp
	Author: GUilherme Bezerra
	Date: 24/06/24 12:21
	Description: Informations about a NFT game to help me in the game's market
*/

// Libraries
#include <stdio.h>
#include <stdlib.h>

// Prototipation
int guildCoin(int, int);
int contribuitionCoin(int, int);
void market();



int main()
{
	// Weekly clan + weekly BossGuild + (weekly diretives)
	int guild_coin = 3000 + 2500 + (7*500);

	//   14/14 - 8/20 -  2/6  -  2/13
	// (Bastium/Celano/Avilius/Tronetel) + bônusBossRaid + (weeklyBossRaid)
	int contribuition_coin = 7*(100+120+50+75) + 500 + (7*100);
	
	while (true)
	{
		system("cls"); // clear
		
    	printf("- weekly guild coin: %i \n"
        	   "- weekly contribuition coin: %i \n\n", guild_coin, contribuition_coin);
        		
        puts("[01] - Guild Coin;\n"
        	 "[02] - Contribuition Coin;\n"
        	 "[03] - Market.");
        	 
        printf("I want to know about: ");
    	int option;
		scanf("%i", &option);
		
		int value;
		int returned;
		switch (option)
		{
			case 1:
				printf("\nHow much I'll need: ");
				scanf("%i", &value);
				
				returned = guildCoin(value, 0);
				printf("\nTotal days to reach the target: %i \n\n", returned);
				
				system("pause"); // wait
				break;
			case 2:
				printf("\nHow much I'll need: ");
				scanf("%i", &value);
				
				returned = contribuitionCoin(value, 0);
				printf("\nTotal days to reach the target: %i \n\n", returned);
				
				system("pause"); // wait
				break;
			case 3:
				market();
				break;
		}
	}
	
	return 0;
} // function end



int guildCoin(int need, int have)
{
	int days = 0;
	int values[50];
	
	while (have < need)
	{
		have += 500;    // diretives daily value
        days += 1;
        values[days-1] = 500;
        
        if ((days % 7) == 0)
        {
        	have += 5500; // weekly "bonus"
        	values[days-1] += 5500; 
		}
	}
	
	int soma = 0;
	for (int i=(days-1); i>=0; i--) // get the array's end
	{
		soma += values[i];
			
		if (i == 0)
			printf("%i = %i", values[i], soma);
		else
		{
			if ((i % 8) == 0)
				puts(""); // line break
			printf("%i+", values[i]);
		}
	}
	
	return days;
} //function end



int contribuitionCoin(int need, int have)
{
	int days = 0;
	int values[50];
	
	while (have < need)
	{
		have += (100+120+50+75) + 100; // coins daily value
        days += 1;
        values[days-1] = (100+120+50+75) + 100;
        
        if ((days % 7) == 0)
        {
        	have += 500; // weekly "bonus"
        	values[days-1] += 500; 
		}
	}
	
	int soma = 0;	
	for (int i=(days-1); i>=0; i--) // get the array's end
	{
		soma += values[i];
			
		if (i == 0)
			printf("%i = %i", values[i], soma);
		else
		{
			if ((i % 8) == 0)
				puts(""); // line break
			printf("%i+", values[i]);
		}
	}
	
	return days;
}



void market()
{
	float bought, recommended, value, total;
	while (true)
	{
		system("cls"); // clear
		
		puts("To go back, type -1");
		printf("Bought value: ");
		scanf("%f", &bought);
		
		recommended = bought + (bought * 0.09);
		
		if (bought == -1) // leave
			return;
			
		while (true)
		{
			printf("\nRecommended> %.0f \n", recommended);
			printf("Value to sell: ");
			scanf("%f", &value);
			
			if (value == -1) // leave
            {				
				printf("");
                break;
            }
            
            total = value - (value * 0.05); // market rate 5%
            if (total > bought)
                printf("PROFIT> ");
            else
                printf("PREJUDICE> ");
                
            printf("%.0f - %.0f = %.0fvdia \n", total, bought, total-bought);
		}
		
	}
}      
