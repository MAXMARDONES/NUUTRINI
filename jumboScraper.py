import gspread
from urllib.request import urlopen
from bs4 import BeautifulSoup
from oauth2client.service_account import ServiceAccountCredentials
from pymongo import MongoClient

client = MongoClient('mongodb://nuutrini:nuutrini123@ds125831.mlab.com:25831/nuutrini')
db = client.nuutrini
products = db.products
"""scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('dev_api_creds.json', scope)
client = gspread.authorize(creds)
sheet = client.open("DATA_OUTLET").sheet1"""

namesArray = []
companyArray = []
pricesArray = []
imagesArray = []
quantityArray = []
splitnameArray = []


def find_links():
    #links_to_scrape = [item for item in sheet.col_values(4) if item][1:]

    links_to_scrape = ["https://nuevo.jumbo.cl/busca/?ft=margarina"]

    for i in range(len(links_to_scrape)):
        print("Scanning: " + links_to_scrape[i])
        html = urlopen(links_to_scrape[i])
        bsObj = BeautifulSoup(html, "html.parser")
        names = bsObj.findAll("a", {"class": "product-item__name"})
        companies = bsObj.findAll("div", {"class": "product-item__brand"})
        prices = bsObj.findAll("span", {"class": "product-prices__value product-prices__value--best-price"})
        images = bsObj.findAll("a", {"class": "product-item__image-link"})

        for name in names:
            namesArray.append(name.get_text())
            prename = name.get_text()
            splitnameArray.append(prename.split(' '))

        for company in companies:
            companyArray.append(company.get_text())
        for price in prices:
            pricesArray.append(price.get_text())
        for image in images:
            imagesArray.append(image.img['src'])

        for b in range(len(names)):
            db.products.insert({
                'name': namesArray[b],
                'company': companyArray[b],
                'price': pricesArray[b],
                'image': imagesArray[b],
                #'quantity': quantityArray[b],
                "category": "MARGARINA"
            })

        print(len(pricesArray))
        print(len(imagesArray))
        print(len(namesArray))

        print(quantityArray)
        print(splitnameArray)
"""
        for x in range(len(splitnameArray)):
            for z in range(len(splitnameArray[x])):
                if splitnameArray[x][z] == 'g,':
                    print("-----FOUND 'g,'--------------------")
                    quantityArray.append(str(splitnameArray[x][z - 1]) + 'g')
                else:
                    if splitnameArray[x][z] == "g":
                        print("------FOUND 'g'------")
                        quantityArray.append(str(splitnameArray[x][z - 1]) + 'g')
                    else:
                        if splitnameArray[x][z] == 'kg':
                            print("------FOUND 'kg'------")
                            quantityArray.append(str(splitnameArray[x][z - 1]) + 'kg')
                        else:
                            if splitnameArray[x][z] == 'Kg':
                                print("------FOUND 'Kg'------")
                                quantityArray.append(str(splitnameArray[x][z - 1]) + 'Kg')
                            else:
                                if splitnameArray[x][z] == 'L':
                                    print("------FOUND 'L'------")
                                    quantityArray.append(str(splitnameArray[x][z - 1]) + 'L')
                                else:
                                    if splitnameArray[x][z] == 'ml':
                                        print("------FOUND 'ml'------")
                                        quantityArray.append(str(splitnameArray[x][z - 1]) + 'ml')
                                    else:
                                        if splitnameArray[x][z] == 'unid':
                                            print("------FOUND 'unid'------")
                                            quantityArray.append(str(splitnameArray[x][z - 1]) + 'unid')
                                        else:
                                            print(quantityArray)
"""


"""

    namesArray quantityArray pricesArray imagesArray
    if (len(namesArray) != len(quantityArray)):
        print("len(namesArray) != len(quantityArray)" + str(len(namesArray) - len(quantityArray)))
    if (len(namesArray) != len(imagesArray)):
        print("len(namesArray) != len(imagesArray)" + str(len(namesArray) - len(imagesArray)))
    if (len(quantityArray) != len(pricesArray)):
        print("len(quantityArray) != len(pricesArray)" + str(len(quantityArray) - len(pricesArray)))
    if (len(imagesArray) != len(quantityArray)):
        print("len(imagesArray) != len(quantityArray)" + str(len(imagesArray) - len(quantityArray)))
    if (len(pricesArray) != len(namesArray)):
        print("len(pricesArray) != len(namesArray)" + str(len(pricesArray) - len(namesArray)))
    if (len(pricesArray) != len(imagesArray)):
        print("len(pricesArray) != len(imagesArray)" + str(len(pricesArray) - len(imagesArray)))
"""










def main():
    find_links()


main()
