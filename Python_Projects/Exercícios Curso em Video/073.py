# Create a tuple with the top 20 placed in the Brazilian Championship Football table, sorted by classification. Show:
# - the top 5 teams
# - the last 4 teams
# - all teams sorted by alphabet
# - what position is the Chapecoense team

teams = ("Corinthians", "Palmeiras", "Santos", "Grêmio", "Cruzeiro", "Flamengo", "Vasco da Gama", "Chapecoense",
         "Atlético", "Botafogo", "Athletico-PR", "Bahia", "São Paulo", "Fluminense", "Sport Recife", "EC Vitória"
         , "Coritiba", "Avaí", "Ponte Preta", "Atlético-GO")

print(f'In the top 5 teams we have {', '.join(teams[0:5])}. \n'
      f'The last 4 teams are {', '.join(teams[len(teams)-4:])}. \n'
      f'All of the 20 team names are {'/'.join(sorted(teams)[:])}. \n'
      f'The Chapecoense team is in {teams.index('Chapecoense')+1}° position.')

input() #wait