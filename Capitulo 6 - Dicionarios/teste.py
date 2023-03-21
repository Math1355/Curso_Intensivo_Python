rios = {'nilo':'egito', 'Amazonas':'brasil', 'kuskokwim':'usa'}

for rio, pais in rios.items():
    print('\n O ' + rio.title() + " corre pelo " + pais.title())

for rio in rios.keys():
    print(rio.title())
    
for pais in rios.values():
    print(pais.title())