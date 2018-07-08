from pymongo import MongoClient
from nuutrini import main 
client = MongoClient('mongodb://nuutrini:nuutrini123@ds125831.mlab.com:25831/nuutrini')
db = client.nuutrini

products = db.products

keyPrice = {}
keyName = {}
keyCategory = {}

d = main()

print(d)
def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

h= remove_duplicates(d)

for j in h:
    print (j)
        
    if products.find({'category':j}):
        products.update({'category': j}, {'$set': {'value': 100}})
    else:
        print(j, 'no existe')
            

    print(keyCategory)


