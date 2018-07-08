import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
 
from pymongo import MongoClient

client = MongoClient('mongodb://nuutrini:nuutrini123@ds125831.mlab.com:25831/nuutrini')
db = client.nuutrini

#existen categories, users, products
categories = db.users

myData = categories.find_one({
	#username va a ser llamado desde la aplicacion web
	'username': 'andres69'
	})

#userChoice es el array con lo que elige la persona
userChoice = myData['mealpreference']

total = len(userChoice)

chilenaCount = 0

clasicaCount = 0

mediterraneoCount = 0

gourmetCount = 0

chilenaPctg = 0

clasicaPctg = 0

mediterraneoPctg = 0

gourmetPctg = 0

for i in range(len(userChoice)):
	if userChoice[i] == "CHILENA":
		chilenaCount += 1

	if userChoice[i] == "CLASICA":
		clasicaCount += 1
	
	if userChoice[i] =="MEDITERRANEA":
		mediterraneoCount += 1

	if userChoice[i] =="GOURMET":
		gourmetCount += 1 

chilenaPctg = float(chilenaCount) / float(total)

clasicoPctg = float(clasicaCount) / float(total)

mediterraneoPctg = float(mediterraneoCount) / float(total)

gourmetPctg = float(gourmetCount) / float(total)

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
 
sheet = client.open("DATA_OUTLET").sheet1
 

# Extract and print all of the values
categories = [item for item in sheet.col_values(2)[1:] if item]
day1 = [item for item in sheet.col_values(3)[1:] if item]
day2 = [item for item in sheet.col_values(4)[1:] if item]
day3 = [item for item in sheet.col_values(5)[1:] if item]
day4 = [item for item in sheet.col_values(6)[1:] if item]
day5 = [item for item in sheet.col_values(7)[1:] if item]
day6 = [item for item in sheet.col_values(8)[1:] if item]
day7 = [item for item in sheet.col_values(9)[1:] if item]


pickerArray = []

def populator(percentage, identifier, pickerArray):
	for i in range(int(percentage*100)):
		pickerArray.append(identifier)

def main():
	populator(chilenaPctg, 'CHILENO', pickerArray)
	populator(gourmetPctg, 'GOURMET', pickerArray)
	populator(mediterraneoPctg, 'MEDITERRANEO', pickerArray)
	populator(clasicoPctg, 'CLASICO', pickerArray)
	random.shuffle(pickerArray)
	picker1 = random.randrange(len(pickerArray) - 1)
	picker2 = random.randrange(len(pickerArray) - 1)
	picker3 = random.randrange(len(pickerArray) - 1)
	picker4 = random.randrange(len(pickerArray) - 1)
	picker5 = random.randrange(len(pickerArray) - 1)
	picker6 = random.randrange(len(pickerArray) - 1)
	picker7 = random.randrange(len(pickerArray) - 1)
	random.shuffle(pickerArray)

	day1 = pickerArray[picker1]
	print(day1, picker1)
	day2 = pickerArray[picker2]
	print(day2, picker2)
	day3 = pickerArray[picker3]
	print(day3, picker3)
	day4 = pickerArray[picker4]
	print(day4, picker4)
	day5 = pickerArray[picker5]
	print(day5, picker5)
	day6 = pickerArray[picker6]
	print(day6, picker6)
	day7 = pickerArray[picker7]
	print(day7, picker7)


	#all_diets = []
	clasicoIndex = [0,3]
	chilenoIndex = [1,2,4,7]
	gourmetIndex = [6,9]
	mediterraneoIndex = [5, 8]

	day1column = sheet.col_values(3)[1:]
	#print(day1column)
	day2column = sheet.col_values(3)[1:]
	#print(day2column)
	day3column = sheet.col_values(3)[1:]
	#print(day3column)
	day4column = sheet.col_values(3)[1:]
	#print(day4column)
	day5column = sheet.col_values(3)[1:]
	#print(day5column)
	day6column = sheet.col_values(3)[1:]
	#print(day6column)
	day7column = sheet.col_values(3)[1:]
	#print(day7column)

	allmealplans = []

	print(day1, day2, day3, day4, day5, day6, day7)
	print(len(pickerArray))

	##STILL NEED TO SPLIT by (' ') and extract categories


	#day1
	if day1 == 'CHILENO':
		value = chilenoIndex[random.randrange(len(chilenoIndex) - 1)]
		allmealplans.append(day1column[value])
		print(value, "1.1")

	if day1 == 'CLASICO':
		value = clasicoIndex[random.randrange(len(clasicoIndex) - 1)]
		allmealplans.append(day1column[value])
		print(value, "1.2")

	if day1 == 'GOURMET':
		value = gourmetIndex[random.randrange(len(gourmetIndex) - 1)]
		allmealplans.append(day1column[value])
		print(value, "1.3")
		print(len(gourmetIndex) - 1)


	if day1 == 'MEDITERRANEO':
		value = mediterraneoIndex[random.randrange(len(mediterraneoIndex) - 1)]
		allmealplans.append(day1column[value])
		print(value, "1.4")
	
    
	#day2
	if day2 == 'CHILENO':
		value = chilenoIndex[random.randrange(len(chilenoIndex) - 1)]
		allmealplans.append(day2column[value])
		print(value, "2.1")

	if day2 == 'CLASICO':
		value = clasicoIndex[random.randrange(len(clasicoIndex) - 1)]
		allmealplans.append(day2column[value])
		print(value, "2.2")

	if day2 == 'GOURMET':
		value = gourmetIndex[random.randrange(len(gourmetIndex) - 1)]
		allmealplans.append(day2column[value])
		print(value, "2.3")

	if day2 == 'MEDITERRANEO':
		value = mediterraneoIndex[random.randrange(len(mediterraneoIndex) - 1)]
		allmealplans.append(day2column[value])
		print(value, "2.4")


	#day3
	if day3 == 'CHILENO':
		value = chilenoIndex[random.randrange(len(chilenoIndex) - 1)]
		allmealplans.append(day3column[value])
		print(value, "3.1")

	if day3 == 'CLASICO':
		value = clasicoIndex[random.randrange(len(clasicoIndex) - 1)]
		allmealplans.append(day3column[value])
		print(value, "3.2")

	if day3 == 'GOURMET':
		value = gourmetIndex[random.randrange(len(gourmetIndex) - 1)]
		allmealplans.append(day3column[value])
		print(value, "3.3")

	if day3 == 'MEDITERRANEO':
		value = mediterraneoIndex[random.randrange(len(mediterraneoIndex) - 1)]
		allmealplans.append(day3column[value])
		print(value, "3.4")


	#day4
	if day4 == 'CHILENO':
		value = chilenoIndex[random.randrange(len(chilenoIndex) - 1)]
		allmealplans.append(day4column[value])
		print(value, "4.1")

	if day4 == 'CLASICO':
		value = clasicoIndex[random.randrange(len(clasicoIndex) - 1)]
		allmealplans.append(day4column[value])
		print(value, "4.2")

	if day4 == 'GOURMET':
		value = gourmetIndex[random.randrange(len(gourmetIndex) - 1)]
		allmealplans.append(day4column[value])
		print(value, "4.3")

	if day4 == 'MEDITERRANEO':
		value = mediterraneoIndex[random.randrange(len(mediterraneoIndex) - 1)]
		allmealplans.append(day4column[value])
		print(value, "4.4")


	#day5
	if day5 == 'CHILENO':
		value = chilenoIndex[random.randrange(len(chilenoIndex) - 1)]
		allmealplans.append(day5column[value])
		print(value, "5.1")

	if day5 == 'CLASICO':
		value = clasicoIndex[random.randrange(len(clasicoIndex) - 1)]
		allmealplans.append(day5column[value])
		print(value, "5.2")

	if day5 == 'GOURMET':
		value = gourmetIndex[random.randrange(len(gourmetIndex) - 1)]
		allmealplans.append(day5column[value])
		print(value, "5.3")

	if day5 == 'MEDITERRANEO':
		value = mediterraneoIndex[random.randrange(len(mediterraneoIndex) - 1)]
		allmealplans.append(day5column[value])
		print(value, "5.4")


	#day6
	if day6 == 'CHILENO':
		value = chilenoIndex[random.randrange(len(chilenoIndex) - 1)]
		allmealplans.append(day6column[value])
		print(value, "6.1")

	if day6 == 'CLASICO':
		value = clasicoIndex[random.randrange(len(clasicoIndex) - 1)]
		allmealplans.append(day6column[value])
		print(value, "6.2")

	if day6 == 'GOURMET':
		value = gourmetIndex[random.randrange(len(gourmetIndex) - 1)]
		allmealplans.append(day6column[value])
		print(value, "6.3")

	if day6 == 'MEDITERRANEO':
		value = mediterraneoIndex[random.randrange(len(mediterraneoIndex) - 1)]
		allmealplans.append(day6column[value])
		print(value, "6.4")


	#day7
	if day7 == 'CHILENO':
		value = chilenoIndex[random.randrange(len(chilenoIndex) - 1)]
		allmealplans.append(day7column[value])
		print(value, "7.1")

	if day7 == 'CLASICO':
		value = clasicoIndex[random.randrange(len(clasicoIndex) - 1)]
		allmealplans.append(day7column[value])
		print(value, "7.2")

	if day7 == 'GOURMET':
		value = gourmetIndex[random.randrange(len(gourmetIndex) - 1)]
		allmealplans.append(day7column[value])
		print(value, "7.3")

	if day7 == 'MEDITERRANEO':
		value = mediterraneoIndex[random.randrange(len(mediterraneoIndex) - 1)]
		allmealplans.append(day7column[value])
		print(value, "7.4")
        
	#allmealplans is an array of string sentences

	all_Categories = []

	for i in range(len(allmealplans)):
		placehold = allmealplans[i].split(" ")
		for x in range(len(placehold)):
			if placehold not in all_Categories:
				all_Categories.append(placehold[x])

				#all_Categories son las categorias que necesitai
	return(all_Categories)









