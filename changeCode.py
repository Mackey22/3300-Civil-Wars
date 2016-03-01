import csv

countryCodes = {'Cambodia': 116, 'Georgia': 268, 'Laos': 418, 'Nepal': 524, 
	'Phillipines': 608, 'Syria': 760, 'Tajikistan': 762, 'Thailand': 764, 
	'Yemen, South': 887, 'Yemen': 887, 'Iran': 364, 'Sri Lanka': 144, 
	'Indonesia': 360, 'Korea North': 408, 'Korea South': 410, 'Afghanistan': 4, 
	'Vietnam, North': 704, 'Vietnam, South': 704, 'Vietnam': 704}

warringYears = {}
for cnt in countryCodes.keys(): 
	warringYears[countryCodes[cnt]] = []

toAdd = []
with open('cWars.csv') as wars: 
	reader = csv.DictReader(wars)
	for row in reader: 
		for cnt in countryCodes.keys(): 
			if cnt == row['COUNTRY']: 
				toWrite = {'Code':(countryCodes[cnt]), 'Country': cnt,  
					'Intensity': row['CIVWAR'], 'Year': row['YEAR']}
				warringYears[countryCodes[cnt]].append(int(row['YEAR']))
				toAdd.append(toWrite)
				continue

with open('cleanWars.csv', 'wb') as cleanWars:
	fields = ['Code', 'Country', 'Intensity', 'Year']
	writer = csv.DictWriter(cleanWars, fieldnames=fields, delimiter=',')
	writer.writeheader()
	writer.writerows(toAdd)

toAddGdp = []
errors = ''
with open('gdp.csv') as gdp:
	reader = csv.DictReader(gdp)
	for row in reader: 
		for cnt in countryCodes.keys():
			if cnt == row['CountryName']:
				for year in warringYears[countryCodes[cnt]]:
					if year < 1960 or row[str(year)] == "":
						errors += ("No GDP value for " + cnt + " in " + str(year) + '\n')
					else: 
						toWrite = {'Code':(countryCodes[cnt]), 'Country': cnt,  
							'GDP': row[str(year)], 'Year': year}
						toAddGdp.append(toWrite)

with open('cleanGdp.csv', 'wb') as cleanGdp:
	fields = ['Code', 'Country', 'GDP', 'Year']
	writer = csv.DictWriter(cleanGdp, fieldnames=fields, delimiter=',')
	writer.writeheader()
	writer.writerows(toAddGdp)

with open('lostGdp.txt', 'wb') as errs: 
	errs.write(errors)







