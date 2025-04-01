# COUPE DE ESCRIVA 2023: FOOTBALL PICKS

print("Welcome to the COUPE DE ESCRIVA 2023: FOOTBALL PICKS \n")

# Dictionary storing the captains of different teams
captain = {'Madiba: ': 'Chubby Obiora-Okafor',
           'Blue-Jays: ': 'Christopher Uweh',
           'Cirok: ': 'Alexander',
           'TSG Walkers: ': 'Ikechukwu'}

# Dictionary storing the goalkeepers of different teams
goalkeepers = {'Madiba: ': 'Chubby Obiora-Okafor',
               'Blue-Jays: ': 'Oladimeji Abaniwondea/Jeffery Awagu',
               'Cirok: ': 'Timileyin Pearse/Izuako Jeremy',
               'TSG Walkers: ': 'Ayomide Ojituku'}

# Loop to print captains
for pick in captain:
    print(pick, captain[pick])

print("\n")  # Print a blank line for separation

# Loop to print goalkeepers
for pick in goalkeepers:
    print(pick, goalkeepers[pick])
